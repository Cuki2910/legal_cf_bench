"""Benchmark v1: item generation, prompts, run, metrics, baselines. See docs/DESIGN_v1.md.

Items are minimal pairs made by TEMPLATE (no LLM):
  base  the case text for one assignment
  F     one known atom flipped using its plain text            (gold changes)
  N3    one known atom flipped using its "near" text           (gold changes)
  S     one unknown atom supplied                              (gold changes)
  N     one known atom re-stated with its "near" text, same value (gold unchanged)
  I1/I2 one irrelevant sentence inserted at end / middle       (gold unchanged)
Gold is computed by logic.gold; nothing is hand-labelled.
"""
from __future__ import annotations

import json
import math
import os
import random
import re

from .logic import ANSWERS, atoms_of, gold
from .rules import RULES

PROMPT_VERSION = "v1"
KINDS = ("F", "N3", "S", "N", "I1", "I2")
FLIPS = ("F", "N3", "S")  # types whose gold must differ from base
FLIP = {"T": "F", "F": "T"}

READING = ('Read "X if and only if C" as: X holds exactly when C holds. '
           'Read "unless E" as: if E holds, X does not hold.')

PA = """Decide the question using ONLY the rule below. Do not use any other law or outside assumptions.
{reading}
A fact that is not stated is unknown, not false. If the stated facts do not settle the question under the rule, answer "undetermined".

Rule: {rule}

Facts:
{facts}

Question: {question}

Reply with JSON only: {{"answer": "yes" | "no" | "undetermined", "deciding_fact": "F<number>" or "none", "explanation": "<one sentence>"}}"""

PB = """Here is a case.
{facts}

Governing rule (the only rule that applies; ignore all other law): {rule}
{reading}
Anything the facts do not mention is unspecified, not false. Answer "undetermined" when the facts given are not enough to settle the question under this rule.

{question}
Return only JSON: {{"answer": "yes" | "no" | "undetermined", "deciding_fact": "<id of the one fact that settles it, like F2, or none>", "explanation": "<one sentence>"}}"""

PROMPTS = {"pA": PA, "pB": PB}


def _render(sents):
    return "\n".join("F%d. %s" % (i + 1, s) for i, s in enumerate(sents))


def build_prompt(item, which="pA"):
    return PROMPTS[which].format(reading=READING, rule=item["rule"], facts=_render(item["facts"]),
                                 question=item["question"])


def _story(rule, assign, variant):
    """-> (sentences, {atom: index of its sentence}). variant: atom -> 0 (plain) | 1 (near). Unknown atoms are omitted."""
    out, pos = [], {}
    for s in rule["facts"]:
        if s.startswith("@"):
            a = s[1:]
            if assign.get(a) in ("T", "F"):
                pos[a] = len(out)
                out.append(rule["atoms"][a][assign[a]][variant.get(a, 0)])
        else:
            out.append(s)
    return out, pos


def _item(rule, base_name, iid, kind, assign, variant, base_gold, extra=None, position="slot", changed=None):
    sents, pos = _story(rule, assign, variant)
    if extra:  # irrelevant sentence
        k = len(sents) if position == "end" else max(1, len(sents) // 2)
        sents.insert(k, extra)
        changed_idx = k + 1
    else:
        changed_idx = pos[changed] + 1 if changed in pos else None
    return dict(id=iid, rule_id=rule["id"], tier=rule["tier"], split=rule["split"], base=base_name, kind=kind,
                position=position, rule=rule["rule"], question=rule["question"], facts=sents,
                gold=gold(rule["formula"], assign), base_gold=base_gold, changed_idx=changed_idx,
                dependent_override=rule["override"])


def generate(rules=RULES):
    items = []
    for r in rules:
        needs = r.get("needs", {})
        for bname, b0 in r["bases"].items():
            bg = gold(r["formula"], b0)
            pre = "%s/%s" % (r["id"], bname)
            items.append(_item(r, bname, pre + "/base", "base", b0, {}, bg))
            for a in sorted(atoms_of(r["formula"])):
                v = b0.get(a)
                if v is None:  # S: supply unknown atom (only if its prerequisites hold)
                    if all(b0.get(p) == "T" for p in needs.get(a, [])):
                        for nv in "TF":
                            asg = dict(b0, **{a: nv})
                            if gold(r["formula"], asg) != bg and gold(r["formula"], asg) != "undetermined":
                                items.append(_item(r, bname, "%s/S.%s%s" % (pre, a, nv), "S", asg, {}, bg, changed=a))
                    continue
                for kind, var in (("F", 0), ("N3", 1)):  # flip
                    asg = dict(b0, **{a: FLIP[v]})
                    if FLIP[v] == "F":  # a failed prerequisite makes dependants meaningless: drop them
                        for d, ps in needs.items():
                            if a in ps:
                                asg.pop(d, None)
                    if gold(r["formula"], asg) != bg:
                        items.append(_item(r, bname, "%s/%s.%s" % (pre, kind, a), kind, asg, {a: var}, bg, changed=a))
                items.append(_item(r, bname, "%s/N.%s" % (pre, a), "N", b0, {a: 1}, bg, changed=a))
            for k, text in enumerate(r["irr"]):
                for p in ("end", "middle"):
                    items.append(_item(r, bname, "%s/I%d.%s" % (pre, k + 1, p), "I%d" % (k + 1), b0, {}, bg,
                                       extra=text, position=p))
    return items


def validate(items):
    """Structural checks: flips change gold, N/I keep it, ids unique, answers legal."""
    seen = set()
    for it in items:
        assert it["id"] not in seen, "dup " + it["id"]
        seen.add(it["id"])
        assert it["gold"] in ANSWERS
        if it["kind"] in FLIPS:
            assert it["gold"] != it["base_gold"], it["id"]
        else:
            assert it["gold"] == it["base_gold"], it["id"]
    return len(items)


# ---------------------------------------------------------------- parsing and baselines

def parse(raw):
    """-> (answer in ANSWERS or None, deciding_fact 'F<k>'|'none'|None)."""
    # Rule fixed before the test run: the model's final answer is the LAST parsable JSON object
    # (some models self-correct and emit several). Flat objects only; our schema has no nesting.
    d = None
    for m in re.finditer(r"\{[^{}]*\}", raw or "", re.S):
        try:
            d = json.loads(m.group(0))
        except Exception:
            pass
    if d is None:
        return None, None
    a = str(d.get("answer", "")).strip().lower()
    f = str(d.get("deciding_fact", "")).strip().upper().replace(" ", "")
    f = f if re.fullmatch(r"F\d+", f) else ("none" if f.lower() == "none" else None)
    return (a if a in ANSWERS else None), f


_STOP = set("a an the of to in on at by for with and or if is are was were be been it its that this who which than then "
            "must may not no only unless within more less after before from as has have had one two exactly shall".split())


def _words(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in _STOP and len(w) > 2}


def baseline_answer(name, it, base_by_key):
    if name == "const-yes":
        return "yes"
    if name == "const-no":
        return "no"
    if name == "const-undetermined":
        return "undetermined"
    if name == "oracle":
        return it["gold"]
    if name == "keyword-trigger":  # copy base gold; if the touched sentence shares a rule word, flip it
        if it["kind"] == "base" or it["changed_idx"] is None:
            return it["base_gold"] if it["kind"] != "base" else it["gold"]
        hit = _words(it["facts"][it["changed_idx"] - 1]) & _words(it["rule"])
        return ({"yes": "no", "no": "yes", "undetermined": "no"}[it["base_gold"]]) if hit else it["base_gold"]
    raise ValueError(name)


# ---------------------------------------------------------------- scoring

def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p, d = k / n, 1 + z * z / n
    c, h = p + z * z / (2 * n), z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round(max(0.0, (c - h) / d), 3), round(min(1.0, (c + h) / d), 3))


def _cluster_ci(rows, B=1000):
    """rows: [(cluster, hit)]. Percentile bootstrap resampling clusters (schemas), seed fixed."""
    by = {}
    for c, h in rows:
        by.setdefault(c, []).append(h)
    ks = list(by)
    if len(ks) < 2:
        return (None, None)
    rng = random.Random(0)
    ests = []
    for _ in range(B):
        s = [h for c in (rng.choice(ks) for _ in ks) for h in by[c]]
        ests.append(sum(s) / len(s))
    ests.sort()
    return (round(ests[int(.025 * B)], 3), round(ests[int(.975 * B) - 1], 3))


def _rate(rows):
    n = len(rows)
    k = sum(h for _, h in rows)
    return {"k": k, "n": n, "rate": round(k / n, 3) if n else None, "ci95_cluster": _cluster_ci(rows)}


def score(items, preds):
    """preds: item id -> {"answer","deciding_fact"}. Returns M0..M5, M7 with unconditional and conditional rates."""
    by_id = {i["id"]: i for i in items}
    base_ok = {(i["rule_id"], i["base"]) for i in items
               if i["kind"] == "base" and preds.get(i["id"], {}).get("answer") == i["gold"]}

    def rows(kinds, cond=False, extra=None):
        out = []
        for i in items:
            if i["kind"] not in kinds or i["id"] not in preds or (extra and not extra(i)):
                continue
            if cond and (i["rule_id"], i["base"]) not in base_ok:
                continue
            out.append((i["rule_id"], preds[i["id"]]["answer"] == i["gold"]))
        return out

    m = {"M0_base_accuracy": _rate(rows(("base",)))}
    for name, kinds in (("M1_flip_sensitivity", FLIPS), ("M2_nearmiss_specificity", ("N",)),
                        ("M3a_irrelevant_plausible", ("I1",)), ("M3b_irrelevant_lexical", ("I2",))):
        m[name] = {"uncond": _rate(rows(kinds)), "cond": _rate(rows(kinds, cond=True))}
    for d in ("yes", "no", "undetermined"):  # M7: direction = base gold
        m["M7_flip_from_" + d] = _rate(rows(FLIPS, extra=lambda i, d=d: i["base_gold"] == d))
    m["by_tier_M1"] = {t: _rate(rows(FLIPS, extra=lambda i, t=t: i["tier"] == t)) for t in (1, 2, 3, 4)}
    m["by_tier_M2"] = {t: _rate(rows(("N",), extra=lambda i, t=t: i["tier"] == t)) for t in (1, 2, 3, 4)}
    cases = {}
    for i in items:
        if i["id"] in preds:
            c = cases.setdefault((i["rule_id"], i["base"]), [])
            c.append(preds[i["id"]]["answer"] == i["gold"])
    m["M4_case_consistency"] = _rate([(k[0], all(v)) for k, v in cases.items()])
    m5 = [(i["rule_id"], preds[i["id"]].get("deciding_fact") == "F%d" % i["changed_idx"])
          for i in items if i["kind"] in FLIPS and i["gold"] != "undetermined" and i["id"] in preds
          and preds[i["id"]]["answer"] == i["gold"]]
    m["M5_deciding_fact_agreement"] = _rate(m5)
    m["unparsable"] = sum(1 for p in preds.values() if p.get("answer") is None)
    m["n_items"] = len(preds)
    return m


def stability(items, pa, pb):
    """M6: share of items whose answer is identical under prompts pA and pB (both parsed)."""
    rows = [(i["rule_id"], pa[i["id"]]["answer"] == pb[i["id"]]["answer"])
            for i in items if i["id"] in pa and i["id"] in pb]
    return _rate(rows)


# ---------------------------------------------------------------- run

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_raw(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf8") as f:
        return [json.loads(l) for l in f if l.strip()]


def run(items, provider, split, which, out_root=None, log=print, limit=None):
    """Append-only raw.jsonl per (provider, split, prompt). Resumable."""
    name = re.sub(r"[^\w.-]", "_", "%s__%s__%s_%s" % (PROMPT_VERSION, provider.name, split, which))
    out = os.path.join(out_root or os.path.join(ROOT, "results"), name)
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "raw.jsonl")
    done = {r["id"] for r in load_raw(path)}
    todo = [i for i in items if i["split"] == split and i["id"] not in done][:limit]
    with open(path, "a", encoding="utf8") as f:
        for it in todo:
            raw = provider.complete(build_prompt(it, which), {})
            a, d = parse(raw)
            f.write(json.dumps({"id": it["id"], "answer": a, "deciding_fact": d, "raw": raw}, ensure_ascii=False) + "\n")
            f.flush()
            log("  %s -> %s" % (it["id"], a))
    return out


def preds_from(path):
    return {r["id"]: r for r in load_raw(os.path.join(path, "raw.jsonl"))}
