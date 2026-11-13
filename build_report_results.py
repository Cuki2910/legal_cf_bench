"""Rebuild numerical appendix from saved runs, without API calls or changing data.

Run: python3 legal_cf_bench/build_report_results.py (from UROP).
Updates only the separate full supplement; creates results CSV/JSON and LaTeX appendix.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import itertools
import json
import random
import sys

ROOT = Path(__file__).resolve().parent
UROP = ROOT.parent
sys.path.insert(0, str(ROOT))
from lcb import v1

MODELS = {"Sol": "gpt-6.1-sol", "Luna": "gpt-6-luna", "Haiku 4.5": "haiku"}
CURRENT = v1.generate()
TEST = [i for i in CURRENT if i["split"] == "test"]
DEV = [i for i in CURRENT if i["split"] == "dev"]
FROZEN = "5a3e55ce1ef6db40db2829e67abfc1dac0748f235fd33d4deb6610e288eb7e2e"
assert hashlib.sha256(json.dumps(TEST, sort_keys=True, ensure_ascii=False).encode()).hexdigest() == FROZEN


def tex(s):
    return str(s).replace("\\", r"\textbackslash{}").replace("_", r"\_").replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")


def fmt(stat):
    return "%d/%d (%.1f\\%%)" % (stat["k"], stat["n"], 100*stat["k"]/stat["n"]) if stat["n"] else "--"


def ci(stat):
    lo, hi = stat["ci95_cluster"]
    return "[%.1f, %.1f]" % (100*lo, 100*hi) if lo is not None else "--"


def table(caption, cols, headers, rows):
    return "\n".join([r"\begingroup\small\setlength{\tabcolsep}{4pt}",
                       r"\begin{longtable}{"+cols+"}",
                       r"\caption{"+caption+r"}\\", r"\toprule",
                       " & ".join(headers)+r" \\", r"\midrule\endfirsthead",
                       r"\toprule", " & ".join(headers)+r" \\", r"\midrule\endhead",
                       r"\bottomrule\endfoot"] + [" & ".join(map(str, row))+r" \\" for row in rows] +
                       [r"\end{longtable}\endgroup", ""])


P, SCORES, ROWS = {}, {}, []
for split, items, prompts in [("dev", DEV, ["pA"]), ("test", TEST, ["pA", "pB"])]:
    for model, needle in MODELS.items():
        for prompt in prompts:
            path = next(p for p in (ROOT/"results").glob("v1__*__%s_%s" % (split, prompt)) if needle in p.name)
            records = v1.load_raw(str(path/"raw.jsonl"))
            assert len({r["id"] for r in records}) == len(records) == len(items)
            preds = {r["id"]: dict(r, answer=v1.parse(r["raw"])[0], deciding_fact=v1.parse(r["raw"])[1]) for r in records}
            assert set(preds) == {i["id"] for i in items}
            P[split, model, prompt] = preds
            score = v1.score(items, preds)
            SCORES["/".join([split, model, prompt])] = score
            for name, stat in score.items():
                if isinstance(stat, dict) and "n" in stat:
                    ROWS.append(dict(split=split, model=model, prompt=prompt, metric=name, condition="all", **stat))
                elif isinstance(stat, dict) and "uncond" in stat:
                    for condition in ["uncond", "cond"]:
                        ROWS.append(dict(split=split, model=model, prompt=prompt, metric=name, condition=condition, **stat[condition]))


def get(split, model, prompt):
    return SCORES["/".join([split, model, prompt])]


out = [r"\clearpage", r"\pagestyle{plain}", r"\appendix", r"\section*{Appendix A. Experimental results and implementation evidence}",
       r"\addcontentsline{toc}{section}{Experimental results}",
       r"\textbf{Interpretation boundary.} All numerical results below are agreement with the current synthetic gold, not validated legal accuracy or a model ranking. Gold was computed from symbolic rules, but a post-run audit found mismatches between some English facts and their intended atom values. Scores are retained without removing disputed items. Human/expert validation of the new item set remains incomplete.",
       r"\textbf{Repository.} \url{https://github.com/Cuki2910/legal_cf_bench/tree/report-v2-validation}. The GitHub repository is public. V1/v2 code and aggregate result files have been pushed to branch report-v2-validation. Raw API responses remain local, so the public aggregates do not independently reproduce provider outputs.",
       r"\textbf{Local evidence.} Counts were recomputed from \path{legal_cf_bench/results/*/raw.jsonl}; v0 values use the saved \path{summary.json}. The frozen test hash matches \path{docs/TEST_FREEZE.txt}. The accompanying \path{docs/REPORT_RESULTS.csv} and \path{docs/REPORT_RESULTS.json} contain the tabulated aggregates; \path{build_report_results.py} rebuilds this appendix without API calls. No raw response was discarded or retried because it was wrong."]

out += [r"\subsection*{A.1 Setup, data sizes and operational definitions}",
        r"The evaluated gateway route labels were \path{cx/gpt-6.1-sol} (Sol), \path{cx/gpt-6-luna[1m]} (Luna), and \path{cc/claude-haiku-4-5-20251001} (Haiku 4.5). These are requested route names; the actual backing model identity was not independently verified. V1 used temperature 0 and a 300-token output limit. Prompt pA and prompt pB differ in wording/order; they are not repeated runs of the same configuration."]
out.append(table("Experiment inventory. Item counts are request-level IDs, not independent observations.", "lrrrr", ["Stage", "Schemas", "Bases", "Items/prompt", "Saved outputs"],
                 [["v0, 2 models, p1", 10, 10, 30, 60], ["v1 dev, 3 models, pA", 7, 21, 235, 705], ["v1 test, 3 models, pA/pB", 8, 24, 239, 1434]]))
out.append(r"The 705 dev and 1,434 test outputs refer to the latest saved run directories. Historical development files overlap later retained records and must not be summed as independent API calls. Dev templates were revised after observing outputs; dev scores are diagnostic only. V1 contains 474 item IDs per prompt across dev and test. Test bases are label-balanced (8 yes, 8 no, 8 undetermined).")
counts = Counter(i["kind"] for i in TEST)
out.append(table("Frozen v1 test composition.", "lrr", ["Condition", "Count", "Expected relation to base"], [["Base", counts["base"], "--"], ["F: plain atom flip", counts["F"], "Gold changes"], ["N3: alternate-text flip", counts["N3"], "Gold changes"], ["S: supply missing atom", counts["S"], "U to yes/no"], ["N: same-value near variant", counts["N"], "Gold unchanged"], ["I1: plausible irrelevant", counts["I1"], "Gold unchanged"], ["I2: harmless irrelevant", counts["I2"], "Gold unchanged"]]))
out.append(r"\textbf{Metrics.} M0: base accuracy. M1: accuracy after F/N3/S; M2: accuracy after N; M3a/M3b: accuracy after I1/I2. Unconditional values compare each target answer with gold; they do not by themselves require a change/stay relative to the model's own base answer. Conditional values restrict to correctly answered bases. M4 requires the base and every intervention within a case to be correct. M5 is a limited proxy: on correctly answered flips with determinate gold, does the one reported fact ID equal the edited fact ID? M6 measures answer agreement between pA and pB, not correctness. M7 separates M1 by base-gold direction. Headline metrics were M1, M2 and M3a; other analyses are supplementary.")
out.append(r"\textbf{Uncertainty.} V1 intervals use percentile cluster bootstrap over schemas (1,000 resamples, seed 0); counts are shown to expose denominators. Eight test clusters are too few for broad generalization. Paired comparison intervals below use 2,000 schema resamples, keep both prompts in each cluster, and have no multiple-comparison correction. These intervals do not account for disputed gold. Degenerate [100,100] conditional intervals only reflect the observed all-correct subset, not certainty about population performance.")

out += [r"\subsection*{A.2 Original pilot v0 (historical; invalid for performance claims)}"]
rows = []
for model, needle in [("Sol", "sol"), ("Luna", "luna")]:
    path = next(p for p in (ROOT/"results").glob("pilot*/summary.json") if needle in p.parent.name)
    s = json.loads(path.read_text())["score"]
    rows.append([model]+[fmt(s[k]) for k in ["base_accuracy", "relevant_sensitivity", "irrelevant_robustness", "explanation_keyword_proxy"]])
out.append(table("Saved v0 results; sensitivity/robustness conditioned on base correctness.", "lrrrr", ["Model", "Base", "Sensitivity", "Robustness", "Keyword proxy"], rows))
out.append(r"V0 had only 10 cases, binary answers, imbalanced base labels, no near-miss category, and ambiguous/manual gold (including a necessary-condition versus sufficient-condition error). Its lexical explanation proxy is not explanation alignment. The results motivated v1 rather than supporting a performance claim. For example, a 10/10 v0 Wilson interval is approximately [72.2,100]\%, illustrating the small sample size.")

out += [r"\subsection*{A.3 Latest development-set results (not held out)}"]
rows=[]
for model in MODELS:
    s=get("dev",model,"pA")
    rows.append([model,fmt(s["M0_base_accuracy"])]+[fmt(s[k]["uncond"]) for k in ["M1_flip_sensitivity","M2_nearmiss_specificity","M3a_irrelevant_plausible","M3b_irrelevant_lexical"]])
out.append(table("Latest v1 dev scores, seven schemas, prompt pA. Gold/template revisions were informed by earlier outputs.", "lrrrrr",["Model","M0","M1","M2","M3a","M3b"],rows))
rows=[]
for model in MODELS:
    s=get("dev",model,"pA")
    rows.append([model,fmt(s["M4_case_consistency"]),fmt(s["M5_deciding_fact_agreement"]),s["unparsable"]])
out.append(table("Development secondary metrics after the final-answer parser was fixed before test.","lrrr",["Model","M4","M5 proxy","Invalid"],rows))
out.append(r"The early four-schema dev set showed ceiling behavior for Sol; three harder schemas were added. Ambiguous examples were subsequently clarified. Those iterations are development decisions, not additional held-out evidence. Haiku's three earlier ``unparsable'' dev responses contained self-corrections with multiple JSON objects; the parser was fixed to take the last parseable object before freezing test. Final dev values above are recomputed from stored raw with that rule.")

out += [r"\subsection*{A.4 Frozen test: all three models and both prompts}"]
for prompt in ["pA","pB"]:
    rows=[]
    for model in MODELS:
        s=get("test",model,prompt)
        rows.append([model,fmt(s["M0_base_accuracy"])]+[fmt(s[k]["uncond"]) for k in ["M1_flip_sensitivity","M2_nearmiss_specificity","M3a_irrelevant_plausible","M3b_irrelevant_lexical"]])
    out.append(table("Test results, "+prompt+", unconditional. All 239 items retained per model.","lrrrrr",["Model","M0","M1","M2","M3a","M3b"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        s=get("test",model,prompt)
        rows.append([model,prompt,ci(s["M0_base_accuracy"])]+[ci(s[k]["uncond"]) for k in ["M1_flip_sensitivity","M2_nearmiss_specificity","M3a_irrelevant_plausible","M3b_irrelevant_lexical"]])
out.append(table("Schema-cluster 95\% intervals for unconditional test rates (percentage points).","llrrrrr",["Model","Prompt","M0","M1","M2","M3a","M3b"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        s=get("test",model,prompt)
        rows.append([model,prompt]+[fmt(s[k]["cond"]) for k in ["M1_flip_sensitivity","M2_nearmiss_specificity","M3a_irrelevant_plausible","M3b_irrelevant_lexical"]])
out.append(table("Test metrics conditional on a correct base. Denominators differ by model.","llrrrr",["Model","Prompt","M1c","M2c","M3ac","M3bc"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        s=get("test",model,prompt)
        for metric in ["M1_flip_sensitivity","M2_nearmiss_specificity","M3a_irrelevant_plausible","M3b_irrelevant_lexical"]:
            v=s[metric]["cond"]
            rows.append([model,prompt,metric.split("_")[0],fmt(v),ci(v)])
out.append(table("Conditional test intervals. Selection on correct bases prevents a like-for-like model comparison.","lllrr",["Model","Prompt","Metric","Correct/eligible","95\% CI"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        s=get("test",model,prompt)
        rows.append([model,prompt,fmt(s["M4_case_consistency"]),ci(s["M4_case_consistency"]),fmt(s["M5_deciding_fact_agreement"]),s["unparsable"]])
out.append(table("Secondary test metrics. M5 is reported for completeness, not as validated alignment.","llrrrr",["Model","Prompt","M4","M4 CI","M5 proxy","Invalid"],rows))
rows=[]
for model in MODELS:
    v=v1.stability(TEST,P["test",model,"pA"],P["test",model,"pB"])
    rows.append([model,fmt(v),ci(v)])
out.append(table("M6: prompt stability across the same 239 test IDs.","lrr",["Model","Same answer pA/pB","95\% CI"],rows))
out.append(r"Haiku pA has one invalid output at \path{dismissal_no_notice/yes/N.A2}; it ends mid-sentence and is counted as incorrect. Finish reason was not saved, so truncation cause is unverified. All other test answers parse. Stability can coexist with consistently wrong answers; it is not an accuracy measure.")

out += [r"\subsection*{A.5 Breakdown by intervention, direction, tier and schema}"]
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        p=P["test",model,prompt]
        vals=[]
        for kind in ["F","N3","S","N","I1","I2"]:
            xs=[i for i in TEST if i["kind"]==kind]
            vals.append("%d/%d"%(sum(p[i["id"]]["answer"]==i["gold"] for i in xs),len(xs)))
        rows.append([model,prompt]+vals)
out.append(table("Correct targets by intervention category; counts, not independent samples.","llrrrrrr",["Model","Prompt","F","N3","S","N","I1","I2"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        p=P["test",model,prompt]
        for source in ["yes","no","undetermined"]:
            for target in ["yes","no","undetermined"]:
                xs=[i for i in TEST if i["kind"] in v1.FLIPS and i["base_gold"]==source and i["gold"]==target]
                if xs:
                    rows.append([model,prompt,tex(source)+r" $\to$ "+tex(target),"%d/%d"%(sum(p[i["id"]]["answer"]==i["gold"] for i in xs),len(xs))])
out.append(table("M7 expanded into actual base-gold to target-gold directions.","lllr",["Model","Prompt","Direction","Correct targets"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        s=get("test",model,prompt)
        for tier in [1,2,3,4]:
            rows.append([model,prompt,"T%d"%tier,fmt(s["by_tier_M1"][tier]),fmt(s["by_tier_M2"][tier])])
out.append(table("Tier breakdown. Tiers are intended structural difficulty, not empirically validated levels.","lllrr",["Model","Prompt","Tier","M1","M2"],rows))
rows=[]
for rid in dict.fromkeys(i["rule_id"] for i in TEST):
    xs=[i for i in TEST if i["rule_id"]==rid]
    vals=[]
    for prompt in ["pA","pB"]:
        for model in MODELS:
            p=P["test",model,prompt]
            vals.append("%d/%d"%(sum(p[i["id"]]["answer"]==i["gold"] for i in xs),len(xs)))
    rows.append([tex(rid)]+vals)
out.append(table("Test accuracy by schema, including base and all interventions.","lrrrrrr",["Schema","Sol A","Luna A","Haiku A","Sol B","Luna B","Haiku B"],rows))
rows=[]
for prompt in ["pA","pB"]:
    for model in MODELS:
        p=P["test",model,prompt]
        c=Counter((i["gold"],p[i["id"]]["answer"]) for i in TEST if i["gold"]!=p[i["id"]]["answer"])
        rows.append([model,prompt]+[c[pair] for pair in [("yes","undetermined"),("no","undetermined"),("yes","no"),("no","yes"),("undetermined","yes"),("undetermined","no")]]+[sum(v for (g,a),v in c.items() if a is None)])
out.append(table("Disagreement counts: expected gold versus observed answer (U = undetermined).","llrrrrrrr",["Model","Prompt",r"Y$\to$U",r"N$\to$U",r"Y$\to$N",r"N$\to$Y",r"U$\to$Y",r"U$\to$N","Invalid"],rows))
out.append(r"Every Sol pA disagreement with gold (58/239) is a yes/no gold paired with an undetermined answer. This is a diagnostic pattern, not proof that all 58 answers are correct: the natural-language entailment must be adjudicated item by item.")

out += [r"\subsection*{A.6 Baselines and paired comparisons}"]
rows=[]
for name in ["const-yes","const-no","const-undetermined","keyword-trigger","oracle"]:
    preds={i["id"]:{"answer":v1.baseline_answer(name,i,None),"deciding_fact":None} for i in TEST}
    s=v1.score(TEST,preds)
    rows.append([tex(name),fmt(s["M0_base_accuracy"])]+[fmt(s[k]["uncond"]) for k in ["M1_flip_sensitivity","M2_nearmiss_specificity","M3a_irrelevant_plausible","M3b_irrelevant_lexical"]])
out.append(table("Model-free test baselines. Oracle is a pipeline check, not a competing baseline.","lrrrrr",["Baseline","M0","M1","M2","M3a","M3b"],rows))
out.append(r"The keyword-trigger baseline is deliberately gold-assisted: it starts from base gold and changes the answer when the edited sentence overlaps rule vocabulary. Its M0=100\% is by construction, not learned performance. It fails near-miss specificity. The criterion that a baseline should not solve all headline metrics excludes oracle, which must score 100\% by construction.")


def paired(a,b,kinds,ws):
    groups={}
    for i in TEST:
        if i["kind"] not in kinds: continue
        for w in ws:
            x=int(P["test",a,w][i["id"]]["answer"]==i["gold"])-int(P["test",b,w][i["id"]]["answer"]==i["gold"])
            groups.setdefault(i["rule_id"],[]).append(x)
    keys=list(groups);rng=random.Random(0); est=[]
    for _ in range(2000):
        values=[v for k in (rng.choice(keys) for _ in keys) for v in groups[k]]
        est.append(sum(values)/len(values))
    est.sort();values=[v for g in groups.values() for v in g]
    return "%.1f [%.1f, %.1f]"%(100*sum(values)/len(values),100*est[50],100*est[1949])
rows=[]
for a,b in [("Sol","Haiku 4.5"),("Sol","Luna"),("Luna","Haiku 4.5")]:
    rows.append([a+" minus "+b]+[paired(a,b,set(v1.KINDS),ws) for ws in [["pA"],["pB"],["pA","pB"]]])
out.append(table("Exploratory paired accuracy difference across all non-base items, percentage points [95\% CI].","lrrr",["Comparison","pA","pB","Pooled prompts"],rows))
rows=[]
for a,b in [("Haiku 4.5","Sol"),("Luna","Sol")]:
    rows.append([a+" minus "+b]+[paired(a,b,kinds,["pA","pB"]) for kinds in [set(v1.FLIPS),{"N"},{"I1"}]])
out.append(table("Exploratory paired differences for each headline metric, pooled prompts.","lrrr",["Comparison","M1","M2","M3a"],rows))
out.append(r"Intervals excluding zero describe differences in agreement with current gold only. They do not rescue gold validity, eliminate multiple-testing effects, or establish one model's superiority. The dev/test ordering reversal must be reported, not optimized away.")

out += [r"\subsection*{A.7 Archived development iterations and validity findings}"]
rows=[]
for d in sorted((ROOT/"results"/"_superseded").rglob("raw.jsonl")):
    recs=v1.load_raw(str(d));model=next(m for m,n in MODELS.items() if n in d.parent.name)
    stage="pre-expansion a" if d.parent.name.endswith("_a") else "pre-expansion b" if d.parent.name.endswith("_b") else "pre-goods-repair c"
    rows.append([stage,model,len(recs),sum(v1.parse(r["raw"])[0] is None for r in recs)])
out.append(table("Saved superseded run snapshots. They overlap later runs; no comparable re-scoring without the exact historical dataset.","llrr",["Snapshot","Model","Records","Invalid under current parser"],rows))
out.append(r"Some intermediate 119-item and 235-item states were not separately snapshotted. The exact historical facts/gold are not versioned for every development round; re-scoring archived answers against today's repaired templates would be misleading. Therefore this table reports verifiable record/parse counts, not reconstructed performance. Small gateway verbatim/style probes were exploratory checks and were not a validated evaluation or fully archived experiment.")
out.append(table("Post-run audit: examples requiring semantic adjudication.","p{3.4cm}p{4.7cm}p{7.1cm}",["Schema","Gold assumption","What the English facts fail to establish"],[
[tex("hotel_safe"),"Watch in safe at theft","Deposited on first day does not entail remained in safe at theft."],
[tex("debt_limitation"),"No written acknowledgment","Never wrote to creditor does not exclude acknowledgment to someone else."],
[tex("dismissal_no_notice"),"No written job protection","No extra agreement does not exclude protection inside the standard employment contract."],
[tex("contract_breach"),"Foreseeable/unforeseeable event","Annual recurrence or historical novelty does not logically settle foreseeability of the specific event."],
["Duplicate stimuli","239 independent texts","There are 183 unique prompts; 46 duplicate groups contain 102 item IDs (56 excess copies)."],
["M5 proxy","Edited fact is the unique deciding fact","Multiple supporting facts and output-format differences are not represented by the single-ID proxy."],
]))
out.append(r"Conditional rates select different base-correct subsets across models, and ambiguous sentences can occur in multiple duplicate stimuli. Cluster resampling handles within-schema dependence but does not remove repeated-stimulus weighting or repair semantic errors. Some v1 flips also drop dependent facts, so not every generated pair is a one-proposition edit. Full detail is in \path{docs/TEST_VALIDITY_AUDIT_v1.md}. No items were removed after seeing test scores.")

out += [r"\subsection*{A.8 Revised implementation status and next experiment}"]
v2=json.loads((ROOT/"data/v2/dataset.json").read_text()); vc=Counter(i["split"] for i in v2["stimuli"]);ec=Counter(e["split"] for e in v2["edges"])
out.append(table("V2 offline implementation only: no model evaluation performed.","lrrr",["Split","Schemas","Unique stimuli","Intervention edges"],[["Repaired inherited dev",15,vc["dev"],ec["dev"]],["New held-out test",4,vc["test"],ec["test"]],["Total",19,len(v2["stimuli"]),len(v2["edges"])]]))
out.append(r"The revised offline implementation now passes 14 regression tests. It separates stimulus IDs from intervention edges, checks exactly one fact-ID change per edge, and cross-checks all read-once three-valued formulas using an independent Boolean-completion evaluator. The v1 schemas are all development data in v2; four new schemas are reserved for a later evaluation. V2 retains the original insurance reporting-possibility exception with explicit possible/impossible facts, rather than silently changing it to another rule. Its runtime can retain full request/response metadata and distinguish prompt variation from repeat agreement. M5 is excluded from ability conclusions.")
out.append(r"\textbf{Remaining work.} Offline checks do not establish natural-language or legal validity. Review the new items, resolve outstanding semantic issues with a second reader where possible, finalize the research question with the supervisor, and only then authorize the next API evaluation. The API gate remains disabled; no v2 model scores are claimed. This project has implemented a fixed-template diagnostic benchmark, not a reliable automated legal Challenger, and has not established novelty or superiority over existing faithfulness methods.")

appendix="\n\n".join(out)+"\n"
(ROOT/"docs/REPORT_RESULTS_APPENDIX.tex").write_text(appendix,encoding="utf8")
(ROOT/"docs/REPORT_RESULTS.json").write_text(json.dumps(SCORES,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
fields=["split","model","prompt","metric","condition","k","n","rate","ci95_cluster"]
with (ROOT/"docs/REPORT_RESULTS.csv").open("w",encoding="utf8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(ROWS)

# Keep the length-limited submission untouched; regenerate only the full supplement.
submission=UROP/"UROP1010_EXPERIMENTAL_SUPPLEMENT.tex"
s=submission.read_text()
s=s.split("% BEGIN GENERATED RESULTS")[0].replace("\\end{document}","").rstrip()
if r"\usepackage{longtable}" not in s:
    s=s.replace(r"\usepackage{array,tabularx,booktabs}",r"\usepackage{array,tabularx,booktabs}"+"\n"+r"\usepackage{longtable}"+"\n"+r"\usepackage[hidelinks]{hyperref}"+"\n"+r"\usepackage{xurl}")
s=s.replace("The revised implementation is in progress; its gold and performance have not yet been validated.","The revised offline implementation is complete and passes regression tests; its natural-language gold and model performance have not yet been validated. Detailed numerical tables, uncertainty estimates, archived-run inventory and the repository link are included in Appendix A.")
# Retain a visible link in the progress section even if the appendix is read separately.
link=r"\textbf{Code reference:} \url{https://github.com/Cuki2910/legal_cf_bench/tree/report-v2-validation} (public; v1/v2 code and aggregates pushed on branch report-v2-validation)."
if link not in s:
    s=s.replace(r"\textbf{Task 4: }",link+"\n\n"+r"\textbf{Task 4: }")
s+="\n\n% BEGIN GENERATED RESULTS\n"+appendix+"\n\\end{document}\n"
# Preserve both earlier report sources before synchronizing their contents.
backup=ROOT/"results/report_source_before_tables";backup.mkdir(parents=True,exist_ok=True)
for name in ["UROP1010_EXPERIMENTAL_SUPPLEMENT.tex"]:
    p=UROP/name;b=backup/name
    if not b.exists(): b.write_bytes(p.read_bytes())
    p.write_text(s,encoding="utf8")
print("Wrote numerical appendix, CSV/JSON and full supplement; submission untouched, no API calls.")
