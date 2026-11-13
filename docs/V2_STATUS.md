# V2 handoff — offline implementation complete, semantic review pending

## Verified locally

- 19 synthetic schemas: 15 repaired inherited dev, 4 new API-held-out test schemas.
- 463 unique stimuli, 478 one-fact intervention edges; no needs/dependent-fact dropping.
- 14 offline tests passed; build and code/dataset hash verification passed.
- Full read-once formula truth-table check against independent Boolean-completion evaluator.
- A01–A05 repairs, explicit thresholds and unknown handling; stimulus content deduplication; separate pair/stimulus metrics; M5 omitted.
- V2 request path saves request and response envelope, prompt/repetition, raw and timestamp; no v2 API calls performed.
- Original insurance reporting-possibility exception retained with explicit possible/impossible statements; did NOT accept the draft's unapproved change to a written-extension exception.

Files: `lcb/v2.py`, `lcb/rules_v2.py`, `tests/test_v2.py`; protocol: `docs/V2_PROTOCOL.md`; review dataset: `data/v2/REVIEW.md`; hashes/gates: `data/v2/manifest.json`; model-free checks: `data/v2/baselines.json`.

## Not complete / not claimed

Human review of generated items and independent second-reader checking are pending/unverified. The inherited schemas include clarified synthetic rule conventions; these must be read as new versioned tasks, not proof of old gold validity. No validated legal performance, no model ranking, no built LLM Challenger, no finalized RQ. No v2 evaluation results. `allow_api=false` protects the approved review-first protocol.

The user has approved finishing the task, but that does not establish missing external validation. This handoff records the actual boundary rather than inventing completion. No further model runs should happen until these gates are addressed. Four test schemas are a small pilot, not enough for broad claims.

## Submission report

`../UROP1010_MIDTERM_REPORT_SUBMISSION.pdf` and `.tex` were produced at UROP root, 3 pages, compiled and visually inspected. They correctly state pilot results are design findings and revised gold/performance unvalidated. The existing `.docx` is older and NOT synchronized; submit the SUBMISSION PDF, not that older Word file. Date 13/11/2026 and Year 2 are inherited fields and need user confirmation if different.

## Commands from legal_cf_bench

```sh
python3 -W error::ResourceWarning -m unittest discover -s tests
python3 -m lcb.v2 check
```

No commit/push or v1 data changes performed for v2. Scope of completion: implementation, offline checks and submission PDF; external semantic validation and API evaluation remain pending.
