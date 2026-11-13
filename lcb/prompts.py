"""Prompt templates. Bump PROMPT_VERSION on any change: it is part of the run id."""
PROMPT_VERSION = "p1"

QA = """Assume ONLY the following rule applies. Do not use any other law.
Rule: {rule}
Case: {facts}
Question: {question}
Reply with JSON only: {{"answer": "yes" or "no", "key_factor": "<short phrase naming the fact that decided your answer>", "explanation": "<1-2 sentences>"}}"""


def build(case, extra_fact: str = "") -> str:
    facts = case.facts + (" " + extra_fact if extra_fact else "")
    return QA.format(rule=case.rule, facts=facts, question=case.question)
