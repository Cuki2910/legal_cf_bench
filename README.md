# legal_cf_bench (pilot)

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
