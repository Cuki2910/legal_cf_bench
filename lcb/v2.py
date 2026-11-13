"""Versioned offline benchmark: python -m lcb.v2 {build,check,run,report}.

V1 data and runs are never rewritten. Stimuli have content IDs; interventions are edges.
ponytail: fixed templates only; add a Challenger after independent semantic validation.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path
import random
import urllib.request
from datetime import datetime, timezone

from .logic import gold, atoms_of

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = {
    "pA": 'Apply ONLY this synthetic rule. "Exactly when" and "if and only if" mean a biconditional. An exception blocks the outcome when its stated condition holds. A condition not stated is unknown, not false. Answer undetermined if the facts do not settle the outcome.\nRule: {rule}\nFacts:\n{facts}\nQuestion: {question}\nReply with one JSON object: {{"answer":"yes|no|undetermined","explanation":"one sentence"}}',
    "pB": 'Decide the question solely under the supplied synthetic rule, ignoring outside law. Missing information is unspecified, not false. Use undetermined if both outcomes remain possible. Read exactly when/if and only if as a biconditional and apply exceptions as written.\n{facts}\nRule: {rule}\n{question}\nReturn a single JSON object with answer (yes, no, or undetermined) and explanation (one sentence).',
}


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Never overwrite a different frozen file silently.
    text = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    if path.exists() and path.read_text() != text:
        raise ValueError("different file already exists: %s" % path)
    path.write_text(text, encoding="utf8")


def independent_gold(formula, assignment):
    """Truth-table completion oracle, independent of logic.ev; for these read-once formulas."""
    def boolean(f, a):
        if isinstance(f, str):
            return a[f]
        if f[0] == "not":
            return not boolean(f[1], a)
        values = [boolean(x, a) for x in f[1:]]
        return all(values) if f[0] == "and" else any(values)
    missing = sorted(atoms_of(formula) - {k for k, v in assignment.items() if v in ("T", "F")})
    fixed = {k: v == "T" for k, v in assignment.items() if v in ("T", "F")}
    outcomes = {boolean(formula, dict(fixed, **dict(zip(missing, vs))))
                for vs in itertools.product((False, True), repeat=len(missing))}
    return "yes" if outcomes == {True} else "no" if outcomes == {False} else "undetermined"


def validate_rule(r):
    names = sorted(atoms_of(r["formula"]))
    def occurrences(f):
        return [f] if isinstance(f, str) else [a for sub in f[1:] for a in occurrences(sub)]
    if len(occurrences(r["formula"])) != len(names):
        raise ValueError("completion cross-check requires read-once formula: " + r["id"])
    if set(names) != set(r["atoms"]) or r.get("needs"):
        raise ValueError("atoms/dependencies: " + r["id"])
    slots = [s[1:] for s in r["facts"] if s.startswith("@")]
    if sorted(slots) != names:
        raise ValueError("each atom needs exactly one slot: " + r["id"])
    for name in names:
        for v in ("T", "F"):
            texts = r["atoms"][name][v]
            if len(texts) != 2 or not all(isinstance(t, str) and t.strip() for t in texts):
                raise ValueError("two nonempty variants required")
    for vs in itertools.product("TFU", repeat=len(names)):
        a = dict(zip(names, vs))
        if gold(r["formula"], a) != independent_gold(r["formula"], a):
            raise ValueError("truth-table mismatch: " + r["id"])
    for expected, a in r["bases"].items():
        if set(a) - set(names) or any(v not in ("T", "F") for v in a.values()):
            raise ValueError("bad base assignment")
        if gold(r["formula"], a) != expected:
            raise ValueError("base label mismatch: " + r["id"])


def generate(rules):
    stimuli, edges, bases = {}, [], []
    def stimulus(r, a, variant=None, extra=None, position="end"):
        facts = []
        for idx, text in enumerate(r["facts"], 1):
            if text.startswith("@"):
                atom = text[1:]
                if atom not in a:
                    continue
                text = r["atoms"][atom][a[atom]][(variant or {}).get(atom, 0)]
            facts.append(["F%d" % idx, text])
        if extra:
            facts.insert(len(facts) if position == "end" else len(facts)//2, ["I", extra])
        content = dict(rule_id=r["id"], rule=r["rule"], question=r["question"], facts=facts)
        sid = digest(content)
        item = dict(content, id=sid, gold=gold(r["formula"], a), split=r["split"], tier=r["tier"])
        if sid in stimuli and stimuli[sid] != item:
            raise ValueError("same text with inconsistent gold/metadata")
        stimuli[sid] = item
        return sid
    for r in rules:
        validate_rule(r)
        for label, a in r["bases"].items():
            source = stimulus(r, a)
            bases.append(dict(rule_id=r["id"], label=label, stimulus=source))
            def edge(target, kind, atom=None, position="slot"):
                edges.append(dict(id="%s/%s/%s/%s/%s" % (r["id"], label, kind, atom or "I", position),
                                  source=source, target=target, kind=kind, atom=atom,
                                  rule_id=r["id"], split=r["split"], position=position))
            for atom in sorted(r["atoms"]):
                if atom in a:
                    b = dict(a, **{atom: "F" if a[atom] == "T" else "T"})
                    if gold(r["formula"], b) != label:
                        edge(stimulus(r, b), "F", atom)
                    edge(stimulus(r, a, {atom: 1}), "N", atom)
                else:
                    for v in "TF":
                        b = dict(a, **{atom: v})
                        if gold(r["formula"], b) != label:
                            edge(stimulus(r, b), "S" + v, atom)
            for j, text in enumerate(r["irr"], 1):
                for pos in ("end", "middle"):
                    edge(stimulus(r, a, extra=text, position=pos), "I%d" % j, position=pos)
    ds = dict(version="v2", stimuli=list(stimuli.values()), bases=bases, edges=edges, prompts=PROMPTS)
    validate(ds)
    return ds


def validate(ds):
    items = {i["id"]: i for i in ds["stimuli"]}
    if len(items) != len(ds["stimuli"]) or len({e["id"] for e in ds["edges"]}) != len(ds["edges"]):
        raise ValueError("duplicate ids")
    for i in items.values():
        content = {k: i[k] for k in ("rule_id", "rule", "question", "facts")}
        if digest(content) != i["id"] or i["gold"] not in ("yes", "no", "undetermined"):
            raise ValueError("invalid stimulus hash/gold")
        if len(dict(i["facts"])) != len(i["facts"]):
            raise ValueError("duplicate fact ids")
    for e in ds["edges"]:
        a, b = items[e["source"]], items[e["target"]]
        fa, fb = dict(a["facts"]), dict(b["facts"])
        changed = {k for k in fa.keys() | fb.keys() if fa.get(k) != fb.get(k)}
        flip = e["kind"] == "F" or e["kind"].startswith("S")
        if len(changed) != 1 or (a["gold"] != b["gold"]) != flip:
            raise ValueError("not a one-fact edge or wrong label: " + e["id"])
        if a["split"] != b["split"] or a["rule_id"] != b["rule_id"]:
            raise ValueError("cross-split/rule edge")


def prompt(item, which):
    return PROMPTS[which].format(rule=item["rule"], question=item["question"],
                                 facts="\n".join("%s. %s" % tuple(f) for f in item["facts"]))


def parse(text):
    decoder, candidates = json.JSONDecoder(), []
    for idx, ch in enumerate(text):
        if ch == "{":
            try:
                obj, _ = decoder.raw_decode(text[idx:])
                if isinstance(obj, dict):
                    candidates.append(obj)
            except ValueError:
                pass
    obj = candidates[-1] if candidates else {}
    answer = obj.get("answer")
    return answer if isinstance(answer, str) and answer in ("yes", "no", "undetermined") else None


def bootstrap(rows):
    groups = {}
    for key, value in rows:
        groups.setdefault(key, []).append(value)
    n, k = len(rows), sum(v for _, v in rows)
    ci = None
    if len(groups) >= 2:
        rng, keys, values = random.Random(0), sorted(groups), []
        for _ in range(2000):
            sample = [v for key in (rng.choice(keys) for _ in keys) for v in groups[key]]
            values.append(sum(sample)/len(sample))
        values.sort(); ci = [values[50], values[1949]]
    return dict(k=k, n=n, rate=k/n if n else None, ci95_schema=ci, clusters=len(groups))


def score(ds, preds, split):
    items = {i["id"]: i for i in ds["stimuli"] if i["split"] == split}
    correct = lambda sid: preds.get(sid) == items[sid]["gold"]
    results = {"unique_stimulus_accuracy": bootstrap([(i["rule_id"], correct(sid)) for sid, i in items.items()])}
    base_ids = {b["stimulus"] for b in ds["bases"] if b["stimulus"] in items}
    results["base_accuracy"] = bootstrap([(items[s]["rule_id"], correct(s)) for s in sorted(base_ids)])
    for name, kinds in [("flip", {"F", "ST", "SF"}), ("near", {"N"}), ("I1", {"I1"}), ("I2", {"I2"})]:
        edges = [e for e in ds["edges"] if e["split"] == split and e["kind"] in kinds]
        results[name] = dict(
            target_accuracy=bootstrap([(e["rule_id"], correct(e["target"])) for e in edges]),
            pair_correct=bootstrap([(e["rule_id"], correct(e["source"]) and correct(e["target"])) for e in edges]),
            conditional=bootstrap([(e["rule_id"], correct(e["target"])) for e in edges if correct(e["source"])]))
    by_rule = {}
    for sid, i in items.items():
        by_rule.setdefault(i["rule_id"], []).append(correct(sid))
    results["by_schema_accuracy"] = {k: dict(k=sum(v), n=len(v), rate=sum(v)/len(v)) for k, v in by_rule.items()}
    results["missing"] = len(set(items) - set(preds))
    results["invalid"] = sum(s in preds and preds[s] is None for s in items)
    return results


def baselines(ds):
    results = {}
    for split in ("dev", "test"):
        items = [i for i in ds["stimuli"] if i["split"] == split]
        results[split] = {}
        for mode in ("yes", "no", "undetermined", "oracle"):
            preds = {i["id"]: i["gold"] if mode == "oracle" else mode for i in items}
            results[split][mode] = score(ds, preds, split)
        oracle = results[split]["oracle"]
        if oracle["unique_stimulus_accuracy"]["rate"] != 1:
            raise ValueError("oracle pipeline failed")
    return results


def build(out):
    from .rules_v2 import RULES
    ds = generate(RULES)
    files = ["v2.py", "rules_v2.py", "logic.py"]
    hashes = {name: hashlib.sha256((ROOT/"lcb"/name).read_bytes()).hexdigest() for name in files}
    manifest = dict(dataset_sha256=digest(ds), code=hashes, human_item_review="pending",
                    second_reviewer="unverified", allow_api=False,
                    note="Assistant checks are not human/expert semantic adjudication.")
    save(out/"dataset.json", ds); save(out/"manifest.json", manifest)
    save(out/"baselines.json", baselines(ds))
    lines = ["# V2 review — human item review PENDING; no model run", ""]
    for i in ds["stimuli"]:
        lines.extend(["## %s / %s / %s" % (i["rule_id"], i["split"], i["id"][:12]),
                      "Rule: " + i["rule"], "Question: " + i["question"],
                      *["%s. %s" % tuple(f) for f in i["facts"]], "Computed gold: `" + i["gold"] + "`", ""])
    text = "\n".join(lines)
    p = out/"REVIEW.md"
    if p.exists() and p.read_text() != text:
        raise ValueError("review already differs")
    p.write_text(text, encoding="utf8")
    print(json.dumps(dict(stimuli=len(ds["stimuli"]), edges=len(ds["edges"]), manifest=manifest), indent=2))


def check(out):
    ds, manifest = json.loads((out/"dataset.json").read_text()), json.loads((out/"manifest.json").read_text())
    validate(ds)
    if digest(ds) != manifest["dataset_sha256"] or ds["prompts"] != PROMPTS:
        raise ValueError("dataset/prompt hash changed")
    for name, h in manifest["code"].items():
        if hashlib.sha256((ROOT/"lcb"/name).read_bytes()).hexdigest() != h:
            raise ValueError("code changed: " + name)
    return ds, manifest


def request(model, text):
    """One request, no content retries. Full JSON/SSE envelope retained without headers/secrets."""
    key = os.environ.get("LCB_API_KEY")
    if not key:
        raise ValueError("LCB_API_KEY not configured")
    body = dict(model=model, temperature=0, max_tokens=1000, stream=False,
                messages=[dict(role="user", content=text)])
    url = (os.environ.get("LCB_BASE_URL") or "https://api.openai.com/v1").rstrip("/") + "/chat/completions"
    req = urllib.request.Request(url, json.dumps(body).encode(),
                                 {"content-type": "application/json", "authorization": "Bearer " + key})
    with urllib.request.urlopen(req, timeout=180) as response:
        data = response.read().decode("utf8")
    if data.lstrip().startswith("data:"):
        events = [json.loads(line[5:]) for line in data.splitlines() if line.startswith("data:") and line[5:].strip() not in ("", "[DONE]")]
        text = "".join(c.get("delta", {}).get("content") or "" for e in events for c in e.get("choices", []) if c.get("index", 0) == 0)
        envelope = dict(sse_events=events)
    else:
        envelope = json.loads(data); text = envelope["choices"][0]["message"]["content"]
    return body, envelope, text


def run(out, model, split, which, repeat):
    ds, manifest = check(out)
    if not manifest.get("allow_api") or manifest.get("human_item_review") != "approved":
        raise ValueError("API blocked: complete human item review and explicitly approve manifest first")
    from .cli import _load_env
    _load_env()
    run_key = digest(dict(dataset=digest(ds), model=model, split=split, prompt=which, repeat=repeat))[:20]
    path = out/"runs"/(run_key + ".jsonl"); path.parent.mkdir(exist_ok=True)
    records = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
    if len({r["id"] for r in records}) != len(records):
        raise ValueError("duplicate run records")
    done = {r["id"] for r in records}
    with path.open("a", encoding="utf8") as f:
        for i in ds["stimuli"]:
            if i["split"] != split or i["id"] in done:
                continue
            text = prompt(i, which)
            body, envelope, raw = request(model, text)
            record = dict(id=i["id"], dataset=digest(ds), model_requested=model, prompt=which,
                          repeat=repeat, request=body, response=envelope, raw=raw, answer=parse(raw),
                          completed_at=datetime.now(timezone.utc).isoformat())
            f.write(json.dumps(record, ensure_ascii=False)+"\n");f.flush();os.fsync(f.fileno())
            print(i["id"][:12], record["answer"], flush=True)
    print(path)


def summarize(out):
    ds, manifest = check(out)
    items = {i["id"]: i for i in ds["stimuli"]}
    runs, results = {}, {}
    for path in sorted((out/"runs").glob("*.jsonl")):
        records = [json.loads(line) for line in path.read_text().splitlines()]
        if not records:
            continue
        first = records[0]
        key = (first["model_requested"], first["prompt"], first["repeat"])
        if key in runs or any((r["model_requested"], r["prompt"], r["repeat"]) != key or r["dataset"] != digest(ds) for r in records):
            raise ValueError("mixed or duplicate runs")
        if len({r["id"] for r in records}) != len(records) or any(r["id"] not in items for r in records):
            raise ValueError("invalid run ids")
        split = items[first["id"]]["split"]
        if any(items[r["id"]]["split"] != split for r in records):
            raise ValueError("mixed splits")
        fullkey = (split,) + key
        preds = {r["id"]: parse(r["raw"]) for r in records}
        runs[fullkey] = preds
        results[" / ".join(map(str, fullkey))] = score(ds, preds, split)
    agreement = {}
    keys = sorted(runs)
    for idx, a in enumerate(keys):
        for b in keys[idx+1:]:
            if a[0] != b[0] or a[1] != b[1]:
                continue
            if (a[2] == b[2]) == (a[3] == b[3]):
                continue  # vary prompt OR repetition, never both
            ids = [sid for sid, i in items.items() if i["split"] == a[0]]
            label = "prompt" if a[3] == b[3] else "repeat"
            rows = [(items[sid]["rule_id"], runs[a].get(sid) is not None and runs[a].get(sid) == runs[b].get(sid)) for sid in ids]
            agreement[str((label, a, b))] = bootstrap(rows)
    output = dict(dataset=manifest["dataset_sha256"], runs=results, agreement=agreement,
                  note="Missing/invalid answers are not agreement. No model ranking without semantic review.")
    # Derived report may be replaced; immutable dataset/manifest and raw are not touched.
    path = out/"run_summary.json"
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf8")
    print(path, "runs", len(runs))


def main():
    ap = argparse.ArgumentParser(__doc__)
    ap.add_argument("command", choices=["build", "check", "run", "report", "summarize"])
    ap.add_argument("--out", type=Path, default=ROOT/"data"/"v2")
    ap.add_argument("--model");ap.add_argument("--split", choices=["dev", "test"], default="test")
    ap.add_argument("--prompt", choices=list(PROMPTS), default="pA")
    ap.add_argument("--repeat", type=int, choices=[1, 2], default=1)
    ap.add_argument("--raw", type=Path)
    args = ap.parse_args()
    if args.command == "build":
        return build(args.out)
    if args.command == "summarize":
        return summarize(args.out)
    ds, manifest = check(args.out)
    if args.command == "check":
        print("verified", manifest)
    elif args.command == "run":
        if not args.model:
            ap.error("--model required")
        run(args.out, args.model, args.split, args.prompt, args.repeat)
    else:
        if not args.raw:
            ap.error("--raw required")
        records = [json.loads(line) for line in args.raw.read_text().splitlines()]
        if len({r["id"] for r in records}) != len(records) or any(r["dataset"] != digest(ds) for r in records):
            raise ValueError("duplicate records or wrong dataset")
        print(json.dumps(score(ds, {r["id"]: parse(r["raw"]) for r in records}, args.split), indent=2))


if __name__ == "__main__":
    main()
