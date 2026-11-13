import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lcb import v1
from lcb.logic import gold


class T(unittest.TestCase):
    def test_kleene(self):
        f = ("and", "A", ("not", "E"))
        self.assertEqual([gold(f, a) for a in ({"A": "T", "E": "F"}, {"A": "T", "E": "T"}, {"A": "T"}, {"A": "F"}, {})],
                         ["yes", "no", "undetermined", "no", "undetermined"])

    def test_generate_valid_and_oracle(self):
        items = v1.generate()
        v1.validate(items)
        p = {i["id"]: {"answer": i["gold"], "deciding_fact": "F%s" % i["changed_idx"]} for i in items}
        m = v1.score(items, p)
        self.assertEqual(m["M1_flip_sensitivity"]["uncond"]["rate"], 1.0)
        self.assertEqual(m["M4_case_consistency"]["rate"], 1.0)

    def test_parse(self):
        self.assertEqual(v1.parse('x {"answer":"Yes","deciding_fact":"f2"} y'), ("yes", "F2"))
        self.assertEqual(v1.parse('```json\n{"answer":"yes","deciding_fact":"F1"}\n```\nWait.\n{"answer":"no","deciding_fact":"F3"}'), ("no", "F3"))
        self.assertEqual(v1.parse("nonsense"), (None, None))
        self.assertEqual(v1.parse('{"answer":"maybe"}')[0], None)


if __name__ == "__main__":
    unittest.main()
