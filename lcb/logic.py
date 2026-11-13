"""3-valued (Kleene) evaluation. Values: "T", "F", "U" (unknown). Formula: atom name | ("not", f) | ("and"|"or", f, ...)."""
from __future__ import annotations

ANSWER = {"T": "yes", "F": "no", "U": "undetermined"}
ANSWERS = tuple(ANSWER.values())


def ev(f, a):
    if isinstance(f, str):
        return a.get(f, "U")
    if f[0] == "not":
        return {"T": "F", "F": "T", "U": "U"}[ev(f[1], a)]
    vs = [ev(x, a) for x in f[1:]]
    if f[0] == "and":
        return "F" if "F" in vs else "U" if "U" in vs else "T"
    if f[0] == "or":
        return "T" if "T" in vs else "U" if "U" in vs else "F"
    raise ValueError("bad op %r" % (f[0],))


def gold(f, a):
    return ANSWER[ev(f, a)]


def atoms_of(f):
    if isinstance(f, str):
        return {f}
    return set().union(*(atoms_of(x) for x in f[1:]))
