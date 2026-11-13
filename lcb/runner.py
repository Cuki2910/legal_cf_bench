"""Run a dataset through a provider. Resumable: raw.jsonl is append-only, finished keys are skipped."""
from __future__ import annotations

import json
import os
import re

from . import prompts
from .metrics import parse_answer, score

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_id(ds, provider):
    return re.sub(r"[^\w.-]", "_", "%s__%s__%s" % (ds.name, provider.name, prompts.PROMPT_VERSION))


def _tasks(ds):
    for c in ds.cases:
        yield c, "base", "", {"expected": c.base_expected, "base_expected": c.base_expected, "keywords": []}
        for ch in c.challenges:
            yield c, ch.id, ch.fact, {"expected": ch.expected, "base_expected": c.base_expected,
                                      "keywords": ch.keywords}


def load_raw(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf8") as f:
        return [json.loads(l) for l in f if l.strip()]


def run(ds, provider, out_root=None, log=print):
    out = os.path.join(out_root or os.path.join(ROOT, "results"), run_id(ds, provider))
    os.makedirs(out, exist_ok=True)
    raw_path = os.path.join(out, "raw.jsonl")
    done = {(r["case"], r["cond"]) for r in load_raw(raw_path)}
    with open(raw_path, "a", encoding="utf8") as f:
        for c, cond, fact, meta in _tasks(ds):
            if (c.id, cond) in done:
                continue
            raw = provider.complete(prompts.build(c, fact), meta)
            ans, text = parse_answer(raw)
            f.write(json.dumps({"case": c.id, "cond": cond, "answer": ans, "text": text, "raw": raw},
                               ensure_ascii=False) + "\n")
            f.flush()  # a crash mid-run keeps everything already paid for
            log("  %s/%s -> %s" % (c.id, cond, ans))
    return report(ds, provider.name, out)


def report(ds, provider_name, out):
    s = score(ds, load_raw(os.path.join(out, "raw.jsonl")))
    meta = {"dataset": ds.name, "provider": provider_name, "prompt_version": prompts.PROMPT_VERSION,
            "score": s}
    with open(os.path.join(out, "summary.json"), "w", encoding="utf8") as f:
        json.dump(meta, f, indent=1)
    return meta
