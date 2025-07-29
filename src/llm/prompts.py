ANALYSIS_PROMPT = """
You are an expert contract lawyer. Carefully review the following contract (governing law: India).
Your output must be formatted in Markdown with clear headings, bullet points, and bold where useful.

For each section, reference any relevant Indian legal considerations. Flag any ambiguous or potentially risky contract language.

Please include:
- **Benefits for the CTO candidate**
- **Concerns or risks (legal, practical, or financial)**
- **Clauses that require clarification or negotiation**
- **Questions to ask before signing**

**Format your output as:**

## Benefits

...

## Concerns

...

## Questions

...

## Summary/Advice

...

Contract text:
{contract}
"""

CRITIC_PROMPT = """
You are a contract law expert. Review the following contract analysis (Markdown). Identify all flaws, gaps, missing legal points, or areas needing clarification, deeper critique, or better practical advice for the CTO. Be specific and detailed.

Previous analysis:
{analysis}
"""

JUDGE_PROMPT = """
You are an impartial contract law reviewer. Given the flaws and gaps found below, give the previous analysis a score out of 10 for:
- Legal coverage
- Depth of analysis
- Practical advice

Explain your score in 2-3 sentences. If any score is below 7, specify why and what should be improved.

List any critical issues that should be addressed in a revision.

Critic findings:
{critic}
Previous analysis:
{analysis}
"""

IMPROVER_PROMPT = """
You are an expert contract lawyer. Given the critic's feedback and the judge's verdict below, rewrite the contract analysis in Markdown.

- Fix all flaws, address all gaps, clarify unclear points, and add any missing sections or advice.
- Use headings (##), bullet points, and **bold** for all new or improved advice.
- Mark substantial new sections with > **Added:** at the start of the bullet or section, for easy review.
- Keep the analysis concise, actionable, and tailored to the CTO’s perspective.
- Do **not** include the contract text itself.

Start with a heading: ## Improved Analysis

Critic findings:
{critic}

Judge's verdict:
{judge}

Previous analysis:
{analysis}
"""
