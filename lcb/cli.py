"""python -m lcb {validate,run}"""
from __future__ import annotations

import argparse
import os

from .providers import ProviderError, get_provider
from .runner import ROOT, run
from .schema import load_dataset

DEFAULT_DATA = os.path.join(ROOT, "data", "cases", "pilot_v0.json")


def _load_env():
    p = os.path.join(ROOT, ".env")  # tiny .env reader; real env vars win
    if os.path.exists(p):
        with open(p, encoding="utf8") as f:
            for l in f:
                l = l.strip()
                if l and not l.startswith("#") and "=" in l:
                    k, v = l.split("=", 1)
                    if v.strip().strip("'\""):  # blank = unset, so provider defaults apply
                        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


def _print(meta):
    print("%s | %s | %s" % (meta["dataset"], meta["provider"], meta["prompt_version"]))
    for k, v in meta["score"].items():
        if isinstance(v, dict):
            print("  %-26s %d/%d  rate=%s  95%%CI=%s" % (k, v["k"], v["n"], v["rate"], v["ci95"]))
        else:
            print("  %-26s %s" % (k, v))


def main(argv=None):
    _load_env()
    ap = argparse.ArgumentParser(prog="lcb")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="check a dataset file")
    v.add_argument("--data", default=DEFAULT_DATA)
    r = sub.add_parser("run", help="run a dataset through a model")
    r.add_argument("--data", default=DEFAULT_DATA)
    r.add_argument("--provider", required=True, help="kind:model, e.g. mock:oracle | anthropic:MODEL | openai:MODEL")
    a = ap.parse_args(argv)
    try:
        ds = load_dataset(a.data)
        if a.cmd == "validate":
            print("ok: %d cases, %d challenges" % (len(ds.cases), sum(len(c.challenges) for c in ds.cases)))
            return 0
        _print(run(ds, get_provider(a.provider)))
        return 0
    except (ProviderError, ValueError) as e:
        print("error:", e)
        return 1
