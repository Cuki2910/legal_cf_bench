"""Dataset schema + validation. One Case = rule + facts + question; challenges are fact additions."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import List

ANSWERS = ("yes", "no")
TYPES = ("relevant", "irrelevant")


@dataclass
class Challenge:
    id: str
    type: str  # relevant: answer should flip; irrelevant: answer should stay
    fact: str
    expected: str
    keywords: List[str] = field(default_factory=list)  # gold cue words for the explanation proxy


@dataclass
class Case:
    id: str
    rule: str
    facts: str
    question: str
    base_expected: str
    challenges: List[Challenge]


@dataclass
class Dataset:
    name: str
    cases: List[Case]


def validate(ds: Dataset) -> List[str]:
    """Return a list of problems (empty = ok)."""
    errs, seen = [], set()
    for c in ds.cases:
        if c.id in seen:
            errs.append("duplicate case id: " + c.id)
        seen.add(c.id)
        if c.base_expected not in ANSWERS:
            errs.append(c.id + ": bad base_expected")
        if not c.challenges:
            errs.append(c.id + ": no challenges")
        cids = set()
        for ch in c.challenges:
            where = "%s/%s" % (c.id, ch.id)
            if ch.id in cids:
                errs.append(where + ": duplicate challenge id")
            cids.add(ch.id)
            if ch.type not in TYPES or ch.expected not in ANSWERS:
                errs.append(where + ": bad type/expected")
            elif ch.type == "relevant" and ch.expected == c.base_expected:
                errs.append(where + ": relevant challenge must flip the answer")
            elif ch.type == "irrelevant" and ch.expected != c.base_expected:
                errs.append(where + ": irrelevant challenge must keep the answer")
    return errs


def load_dataset(path: str) -> Dataset:
    with open(path, encoding="utf8") as f:
        raw = json.load(f)
    cases = [Case(id=c["id"], rule=c["rule"], facts=c["facts"], question=c["question"],
                  base_expected=c["base_expected"],
                  challenges=[Challenge(**ch) for ch in c["challenges"]]) for c in raw["cases"]]
    ds = Dataset(raw["name"], cases)
    errs = validate(ds)
    if errs:
        raise ValueError("invalid dataset:\n  " + "\n  ".join(errs))
    return ds
