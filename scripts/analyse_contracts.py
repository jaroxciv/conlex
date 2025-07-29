# scripts/analyse_contracts.py

import os
import argparse
from conlex.io.loader import load_contract
from conlex.llm.reflexion import analyse_contract
from loguru import logger


DATA_DIR = "data"
OUTPUTS_DIR = "outputs"

def analyse_file(input_filename):
    in_path = os.path.join(DATA_DIR, input_filename)
    out_path = os.path.join(OUTPUTS_DIR, input_filename.replace(".docx", "_analysis.md"))
    logger.info(f"Starting analysis for: {input_filename}")
    text = load_contract(in_path)
    logger.debug(f"Contract preview: {text[:300]}{'...' if len(text) > 300 else ''}")
    analysis = analyse_contract(text)
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(analysis)
    logger.success(f"Analysis for {input_filename} saved to {out_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Contract LLM Self-Reflexive Analyzer"
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Contract .docx files (must exist in ./data/)"
    )
    parser.add_argument(
        "--synthesize", action="store_true",
        help="After analyzing all contracts, synthesize a joint analysis (for two files only)."
    )
    args = parser.parse_args()

    analysed_files = []
    for filename in args.files:
        analyse_file(filename)
        out_path = os.path.join(OUTPUTS_DIR, filename.replace(".docx", "_analysis.md"))
        with open(out_path, "r", encoding="utf-8") as f:
            analysed_files.append(f.read())

    # If requested, run synthesis
    if args.synthesize and len(analysed_files) == 2:
        from conlex.llm.synthesizer import synthesize_analyses
        synthesis = synthesize_analyses(analysed_files[0], analysed_files[1])
        synth_path = os.path.join(OUTPUTS_DIR, "synthesis_analysis.md")
        with open(synth_path, "w", encoding="utf-8") as f:
            f.write(synthesis)
        logger.success(f"Synthesized analysis saved to {synth_path}")

if __name__ == "__main__":
    main()
