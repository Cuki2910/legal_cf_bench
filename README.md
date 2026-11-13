# legal_cf_bench — synthetic-rule pilot and validation audit

## Current status (v1/v2)

- **V1:** 3 gateway model routes, 2 test prompts, 1,434 test responses. The audit found ambiguous fact-to-atom mappings and repeated stimuli; scores are **not a validated model ranking**. See [test results](docs/TEST_RESULTS_v1.md) and [validity audit](docs/TEST_VALIDITY_AUDIT_v1.md).
- **V2 offline:** 19 schemas, 463 unique stimuli, 478 intervention edges; 14 regression tests pass. Human item review is pending, a second reader is unverified, and API evaluation is blocked by default. No v2 model scores or automated LLM Challenger are claimed.
- Repaired v1 schemas are dev-only in v2. Four new synthetic schemas are reserved for later API evaluation. Synthetic rules are not real law.

```sh
python3 -W error::ResourceWarning -m unittest discover -s tests
python3 -m lcb.v2 check
```

Published review artifacts: [v2 items](data/v2/REVIEW.md), [manifest](data/v2/manifest.json), [protocol](docs/V2_PROTOCOL.md), [aggregate results](docs/REPORT_RESULTS.json). Raw API responses remain local under ignored `results/`; aggregates alone do not independently reproduce those responses. `build_report_results.py` rebuilds the full supplement from those local runs and the report sources in the parent UROP directory; it is not a standalone fresh-clone report builder.

The original v0 interface below remains available for historical reproduction; its binary gold and explanation proxy were not validated. Do not use v0 to rank models.

## Original v0 pilot


Behavioral counterfactual-challenge check for Legal QA. For each case: the base question, plus
fact additions that should change the answer (relevant) or not (irrelevant). Stdlib only, Python 3.9+.

**Status: pilot.** Cases are hand-written with SYNTHETIC rules stated in the prompt (not real law).
Challenges are fixed (no Challenger yet). Numbers are descriptive on a tiny set, not validated metrics.
Reports observable decision behavior only; says nothing about the model's internal reasoning.

## Run (from this folder)
```bash
python3 -m unittest discover -s tests                 # offline checks
python3 -m lcb validate                               # check dataset
python3 -m lcb run --provider mock:oracle             # offline dry run
cp .env.example .env                                  # put LCB_API_KEY in it
python3 -m lcb run --provider anthropic:MODEL_ID      # real run (or openai:MODEL_ID, + LCB_BASE_URL)
```
Output: `results/<dataset>__<provider>__<prompt_version>/{raw.jsonl,summary.json}`. Runs resume:
re-running skips finished (case, condition) pairs.

## Layout
| Path | Role |
|---|---|
| `lcb/schema.py` | Case/Challenge dataclasses + validation (relevant must flip, irrelevant must keep) |
| `lcb/prompts.py` | prompt template + `PROMPT_VERSION` (part of the run id) |
| `lcb/providers.py` | mock / anthropic / openai-compatible; reads `LCB_*` env only |
| `lcb/runner.py` | resumable run loop, raw log, summary |
| `lcb/metrics.py` | sensitivity, robustness, keyword proxy, Wilson 95% CI |
| `data/cases/` | datasets (`pilot_v0.json`) |
| `tests/` | offline unit tests |

## Metrics (all conditioned on correct base answer)
- relevant_sensitivity: answer changed to the expected one after a relevant fact.
- irrelevant_robustness: answer unchanged after an irrelevant fact.
- explanation_keyword_proxy: among correct flips, explanation mentions a gold cue word. Crude string match, NOT explanation alignment.

## Known limits
- n=10 cases: read the CI, not the rate.
- Synthetic rules: self-written, so expected outcomes are logic, not law.
- Keyword proxy rewards wording, not understanding.
- Not yet: Challenger generation, real statutes/cases, expert-checked labels, multi-factor interactions, multiple seeds.

## Where to extend
New dataset: add a JSON in `data/cases/`, pass `--data`. New model API: add a class in `providers.py`.
Challenger: generate `challenges` into the same schema, then `validate` and run unchanged.
