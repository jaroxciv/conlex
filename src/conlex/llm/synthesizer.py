from conlex.llm.engine import call_llm
from conlex.llm.prompts import SYNTHESIS_PROMPT
from loguru import logger

def synthesize_analyses(equity_md, sha_md):
    logger.info("Running synthesis of equity and SHA analyses...")
    synthesis = call_llm(SYNTHESIS_PROMPT.format(
        equity_analysis=equity_md,
        sha_analysis=sha_md
    ))
    logger.success("Synthesis complete.")
    return synthesis
