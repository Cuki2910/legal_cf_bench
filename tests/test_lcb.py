"""python3 -m unittest discover -s tests   (from legal_cf_bench/). Offline: mock providers only."""
import copy
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lcb import metrics, schema
from lcb.cli import DEFAULT_DATA
from lcb.providers import Mock, ProviderError, get_provider
from lcb.runner import load_raw, run


class T(unittest.TestCase):
    def setUp(self):
        self.ds = schema.load_dataset(DEFAULT_DATA)

    def _run(self, mode, root):
        return run(self.ds, Mock(mode), out_root=root, log=lambda *_: None)["score"]

    def test_oracle_and_const(self):
        with tempfile.TemporaryDirectory() as d:
            o = self._run("oracle", d)
            k = self._run("const", d)
        n = len(self.ds.cases)
        self.assertEqual((o["relevant_sensitivity"]["k"], o["irrelevant_robustness"]["k"]), (n, n))
        self.assertEqual(o["explanation_keyword_proxy"]["k"], n)
        # always repeating the base answer: perfectly 'robust', never sensitive
        self.assertEqual((k["relevant_sensitivity"]["k"], k["irrelevant_robustness"]["k"]), (0, n))

    def test_resume_skips_finished(self):
        with tempfile.TemporaryDirectory() as d:
            self._run("oracle", d)
            self._run("oracle", d)  # second run must not duplicate rows
            rows = load_raw(os.path.join(d, os.listdir(d)[0], "raw.jsonl"))
        self.assertEqual(len(rows), sum(1 + len(c.challenges) for c in self.ds.cases))

    def test_wrong_base_not_credited(self):
        recs = [{"case": c.id, "cond": "base", "answer": "yes" if c.base_expected == "no" else "no", "text": ""}
                for c in self.ds.cases]
        s = metrics.score(self.ds, recs)
        self.assertEqual((s["base_accuracy"]["k"], s["irrelevant_robustness"]["n"]), (0, 0))

    def test_parse_and_wilson(self):
        self.assertEqual(metrics.parse_answer('x {"answer":"Yes","key_factor":"a","explanation":"b"} y')[0], "yes")
        self.assertIsNone(metrics.parse_answer("no json")[0])
        lo, hi = metrics.wilson(7, 10)
        self.assertTrue(lo < 0.7 < hi and hi - lo > 0.3)  # n=10 -> wide interval
        self.assertEqual(metrics.wilson(0, 0), (None, None))

    def test_validate_rejects_bad_challenges(self):
        bad = copy.deepcopy(self.ds)
        c = bad.cases[0]
        c.challenges[0].expected = c.base_expected  # 'relevant' that does not flip
        self.assertTrue(schema.validate(bad))

    def test_provider_specs(self):
        with self.assertRaises(ProviderError):
            get_provider("nocolon")
        with self.assertRaises(ProviderError):
            get_provider("foo:bar")


if __name__ == "__main__":
    unittest.main()
