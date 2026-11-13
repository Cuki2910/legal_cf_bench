"""Behavioral metrics over raw records. These are PILOT descriptive numbers, not validated metrics.

Records: {"case": id, "cond": "base"|<challenge id>, "answer": "yes"|"no"|None, "text": str}
Sensitivity/robustness are conditioned on the base answer being correct, so a model that is wrong
on the original case is not credited for 'staying stable' or 'flipping'.
"""
from __future__ import annotations

import json
import math
import re


def parse_answer(raw):
    """-> (answer or None, explanation text). Unparsable output gives (None, raw)."""
    m = re.search(r"\{.*\}", raw, re.S)
    try:
        d = json.loads(m.group(0))
        a = str(d.get("answer", "")).strip().lower()
        return (a if a in ("yes", "no") else None), "%s %s" % (d.get("key_factor", ""), d.get("explanation", ""))
    except Exception:
        return None, raw


def wilson(k, n, z=1.96):
    """95% Wilson interval; wide when n is small -- print it so 7/10 is not over-read."""
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round(max(0.0, (c - h) / d), 3), round(min(1.0, (c + h) / d), 3))


def _stat(k, n):
    return {"k": k, "n": n, "rate": (round(k / n, 3) if n else None), "ci95": wilson(k, n)}


def score(ds, records):
    g = {(r["case"], r["cond"]): r for r in records}
    base_ok = [c for c in ds.cases if (c.id, "base") in g and g[(c.id, "base")]["answer"] == c.base_expected]
    sens, rob, align = [], [], []
    for c in base_ok:
        for ch in c.challenges:
            r = g.get((c.id, ch.id))
            if r is None:
                continue
            hit = r["answer"] == ch.expected
            if ch.type == "relevant":
                sens.append(hit)
                if hit and ch.keywords:
                    align.append(any(k.lower() in r["text"].lower() for k in ch.keywords))
            else:
                rob.append(hit)
    n_base = sum(1 for c in ds.cases if (c.id, "base") in g)
    return {
        "n_cases": len(ds.cases),
        "base_accuracy": _stat(len(base_ok), n_base),
        "relevant_sensitivity": _stat(sum(sens), len(sens)),
        "irrelevant_robustness": _stat(sum(rob), len(rob)),
        "explanation_keyword_proxy": _stat(sum(align), len(align)),
        "unparsable": sum(1 for r in records if r["answer"] is None),
    }
