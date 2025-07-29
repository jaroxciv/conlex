from conlex.llm.engine import call_llm
from conlex.llm.prompts import (
    ANALYSIS_PROMPT, CRITIC_PROMPT, JUDGE_PROMPT, IMPROVER_PROMPT
)
from conlex.utils.chunk import chunk_text
from loguru import logger

def analyse_contract(text):
    analyses = []
    logger.info("=== Starting contract analysis pipeline ===")
    for i, chunk in enumerate(chunk_text(text, max_words=2000), 1):
        logger.info(f"[Analysis] Analysing chunk {i}")
        logger.debug(f"[Analysis] Chunk {i} preview: {chunk[:200]}{'...' if len(chunk) > 200 else ''}")
        analysis = call_llm(ANALYSIS_PROMPT.format(contract=chunk))
        logger.debug(f"[Analysis] Chunk {i} analysis preview: {analysis[:300]}{'...' if len(analysis) > 300 else ''}")
        analyses.append(analysis)
    merged = "\n\n".join(analyses)
    logger.info(f"[Analysis] Completed {len(analyses)} chunk(s), merged for reflexion.")

    # Step 1: Critic
    logger.info("[Critic] Reviewing merged analysis for flaws, gaps, or missing legal points.")
    critic = call_llm(CRITIC_PROMPT.format(analysis=merged))
    logger.debug(f"[Critic] Findings preview: {critic[:400]}{'...' if len(critic) > 400 else ''}")

    # Step 2: Judge
    logger.info("[Judge] Scoring analysis and highlighting critical issues.")
    judge = call_llm(JUDGE_PROMPT.format(critic=critic, analysis=merged))
    logger.debug(f"[Judge] Verdict preview: {judge[:400]}{'...' if len(judge) > 400 else ''}")

    # Step 3: Improver
    logger.info("[Improver] Rewriting analysis in Markdown, applying all feedback.")
    improved = call_llm(IMPROVER_PROMPT.format(critic=critic, judge=judge, analysis=merged))
    logger.success("=== Self-reflexion complete. Improved analysis ready. ===")

    return improved
