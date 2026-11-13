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
    au = sub.add_parser("audit", help="v1: write every generated item (facts + computed gold) for human review")
    au.add_argument("--out", default=os.path.join(ROOT, "docs", "ITEMS_v1.md"))
    b = sub.add_parser("baselines", help="v1: score model-free baselines")
    r1 = sub.add_parser("run1", help="v1: run a model on one split and prompt")
    r1.add_argument("--provider", required=True)
    r1.add_argument("--split", choices=("dev", "test"), required=True)
    r1.add_argument("--prompt", choices=("pA", "pB"), default="pA")
    r1.add_argument("--limit", type=int)
    rp = sub.add_parser("report1", help="v1: score finished run dirs")
    rp.add_argument("dirs", nargs="+")
    a = ap.parse_args(argv)
    if a.cmd in ("audit", "baselines", "run1", "report1"):
        return _v1(a)
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


def _v1(a):
    import json

    from . import v1
    items = v1.generate()
    v1.validate(items)
    if a.cmd == "audit":
        with open(a.out, "w", encoding="utf8") as f:
            f.write("# Items v1 (generated; gold computed from formula). Kiet: mark any item whose gold you dispute.\n\n")
            last = None
            for i in items:
                if i["rule_id"] != last:
                    last = i["rule_id"]
                    f.write("\n## %s (tier %d, %s)\nRULE: %s\nQ: %s\n" % (last, i["tier"], i["split"], i["rule"], i["question"]))
                f.write("\n**%s**  gold=`%s` (base `%s`)  kind=%s pos=%s\n" % (i["id"], i["gold"], i["base_gold"], i["kind"], i["position"]))
                f.write("\n".join("  F%d. %s" % (k + 1, t) for k, t in enumerate(i["facts"])) + "\n")
        print("wrote", a.out, len(items), "items")
        return 0
    if a.cmd == "baselines":
        for name in ("const-yes", "const-no", "const-undetermined", "keyword-trigger", "oracle"):
            preds = {i["id"]: {"answer": v1.baseline_answer(name, i, None), "deciding_fact": None} for i in items}
            m = v1.score(items, preds)
            print("%-19s M0=%s M1=%s M2=%s M3a=%s M3b=%s" % (
                name, m["M0_base_accuracy"]["rate"], m["M1_flip_sensitivity"]["uncond"]["rate"],
                m["M2_nearmiss_specificity"]["uncond"]["rate"], m["M3a_irrelevant_plausible"]["uncond"]["rate"],
                m["M3b_irrelevant_lexical"]["uncond"]["rate"]))
        return 0
    if a.cmd == "run1":
        try:
            print(v1.run(items, get_provider(a.provider), a.split, a.prompt, limit=a.limit))
            return 0
        except ProviderError as e:
            print("error:", e)
            return 1
    for d in a.dirs:  # report1
        print(d)
        print(json.dumps(v1.score([i for i in items if True], v1.preds_from(d)), indent=1))
    return 0
