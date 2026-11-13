"""Model providers. Spec format: "<kind>:<model>", e.g. mock:oracle, anthropic:MODEL, openai:MODEL.

Real providers read LCB_API_KEY (+ optional LCB_BASE_URL) -- deliberately NOT the generic
ANTHROPIC_*/OPENAI_* names, so a tool's internal gateway is never picked up by accident.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request


class ProviderError(RuntimeError):
    pass


def _post(url, headers, body, tries=3):
    data = json.dumps(body).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data, dict(headers, **{"content-type": "application/json"}))
            with urllib.request.urlopen(req, timeout=90) as r:
                return _body(r.read())
        except urllib.error.HTTPError as e:
            detail = e.read()[:300].decode("utf8", "replace")
            if e.code in (429, 500, 502, 503, 529) and i < tries - 1:
                time.sleep(2 ** (i + 1))
                continue
            raise ProviderError("HTTP %s from %s: %s" % (e.code, url, detail))
        except urllib.error.URLError as e:
            if i < tries - 1:
                time.sleep(2 ** (i + 1))
                continue
            raise ProviderError("network error: %s" % e)


def _body(b):
    """Some gateways answer with an SSE stream even when stream was not requested: fold it into one completion."""
    t = b.decode("utf8", "replace")
    if not t.lstrip().startswith("data:"):
        return json.loads(t)
    parts = []
    for l in t.splitlines():
        if l.startswith("data:") and l[5:].strip() not in ("", "[DONE]"):
            for c in json.loads(l[5:]).get("choices", []):
                parts.append((c.get("delta") or {}).get("content") or "")
    return {"choices": [{"message": {"content": "".join(parts)}}]}


def _key():
    k = os.environ.get("LCB_API_KEY")
    if not k:
        raise ProviderError("LCB_API_KEY not set (see .env.example)")
    return k


class Mock:
    """Offline stand-in for tests/dry-runs. oracle = always correct; const = repeats the base answer."""

    def __init__(self, mode):
        if mode not in ("oracle", "const"):
            raise ProviderError("mock mode must be oracle|const")
        self.mode = mode
        self.name = "mock-" + mode

    def complete(self, prompt, meta):
        a = meta["expected"] if self.mode == "oracle" else meta["base_expected"]
        kf = " ".join(meta["keywords"]) if self.mode == "oracle" else ""
        return json.dumps({"answer": a, "key_factor": kf, "explanation": ""})


class Anthropic:
    def __init__(self, model):
        self.model, self.name = model, "anthropic-" + model
        self.base = (os.environ.get("LCB_BASE_URL") or "https://api.anthropic.com").rstrip("/")

    def complete(self, prompt, meta):
        url = self.base + ("/messages" if self.base.endswith("/v1") else "/v1/messages")
        h = {"x-api-key": _key(), "anthropic-version": "2023-06-01"}
        r = _post(url, h, {"model": self.model, "max_tokens": 300, "temperature": 0,
                           "messages": [{"role": "user", "content": prompt}]})
        return r["content"][0]["text"]


class OpenAICompat:
    def __init__(self, model):
        self.model, self.name = model, "openai-" + model
        self.base = (os.environ.get("LCB_BASE_URL") or "https://api.openai.com/v1").rstrip("/")

    def complete(self, prompt, meta):
        r = _post(self.base + "/chat/completions", {"authorization": "Bearer " + _key()},
                  {"model": self.model, "max_tokens": 300, "temperature": 0,
                   "messages": [{"role": "user", "content": prompt}]})
        return r["choices"][0]["message"]["content"]


def get_provider(spec):
    kind, _, model = spec.partition(":")
    if not model:
        raise ProviderError("provider spec must be kind:model, got %r" % spec)
    kinds = {"mock": Mock, "anthropic": Anthropic, "openai": OpenAICompat}
    if kind not in kinds:
        raise ProviderError("unknown provider kind %r (use %s)" % (kind, "|".join(kinds)))
    return kinds[kind](model)
