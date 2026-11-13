"""Offline: python3 -m unittest discover -s tests. No API credentials required."""
import copy
import itertools
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lcb import v2
from lcb.logic import gold


def toy():
    return dict(id="toy", split="test", tier=2,
                rule="X exactly when A and not E.", question="X?", formula=("and", "A", ("not", "E")),
                facts=["A fictional case.", "@A", "@E"],
                atoms={"A": {"T": ["A holds.", "A still holds."], "F": ["A does not hold.", "A still does not hold."]},
                       "E": {"T": ["E holds.", "E still holds."], "F": ["E does not hold.", "E still does not hold."]}},
                bases={"yes": {"A": "T", "E": "F"}, "no": {"A": "T", "E": "T"}, "undetermined": {"A": "T"}},
                irr=["The room is blue.", "The table is round."])


class V2(unittest.TestCase):
    def test_truth_tables(self):
        for op in ["and", "or"]:
            for vs in itertools.product("TFU", repeat=3):
                a = dict(zip("ABC", vs)); f = (op, "A", ("not", (op, "B", "C")))
                self.assertEqual(gold(f, a), v2.independent_gold(f, a))

    def test_edges_and_unique_stimuli(self):
        ds = v2.generate([toy()]); v2.validate(ds)
        self.assertEqual(len(ds["stimuli"]), len({i["id"] for i in ds["stimuli"]}))
        preds = {i["id"]: i["gold"] for i in ds["stimuli"]}
        m = v2.score(ds, preds, "test")
        self.assertEqual(m["unique_stimulus_accuracy"]["rate"], 1)
        for name in ["flip", "near", "I1", "I2"]:
            self.assertEqual(m[name]["pair_correct"]["rate"], 1)
        self.assertEqual(v2.score(ds, {}, "test")["missing"], len(preds))
        self.assertEqual(v2.score(ds, {}, "test")["flip"]["pair_correct"]["rate"], 0)
        broken = copy.deepcopy(ds)
        broken["stimuli"][0]["facts"].append(["BAD", "A second changed fact."])
        with self.assertRaises(ValueError):
            v2.validate(broken)

    def test_no_dependencies_or_duplicate_slots(self):
        r = toy();r["needs"] = {"E": ["A"]}
        with self.assertRaises(ValueError):
            v2.generate([r])
        r = toy();r["facts"].append("@A")
        with self.assertRaises(ValueError):
            v2.generate([r])

    def test_parser(self):
        self.assertEqual(v2.parse('{"answer":"no","explanation":"a {brace} in text"}'), "no")
        self.assertEqual(v2.parse('{"answer":"yes"} then {"answer":"no"}'), "no")
        self.assertIsNone(v2.parse('{"answer":["yes"]}'))
        self.assertIsNone(v2.parse('not JSON'))

    def test_actual_schemas(self):
        from lcb.rules_v2 import RULES
        from lcb.rules import RULES as V1
        ds = v2.generate(RULES)
        old_ids = {r["id"] for r in V1}
        self.assertTrue(all(r["split"] == "dev" for r in RULES if r["id"] in old_ids))
        self.assertGreaterEqual(len([r for r in RULES if r["split"] == "test"]), 4)
        self.assertTrue(all(r["id"] not in old_ids for r in RULES if r["split"] == "test"))
        self.assertEqual(len({r["id"] for r in RULES}), len(RULES))
        self.assertTrue(all(i["gold"] in ["yes", "no", "undetermined"] for i in ds["stimuli"]))


if __name__ == "__main__":
    unittest.main()
