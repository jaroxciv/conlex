# scripts/analyse_contracts.py

import os
import argparse
from src.io.loader import load_contract
from src.llm.reflexion import analyse_contract
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
    args = parser.parse_args()
    for filename in args.files:
        analyse_file(filename)

if __name__ == "__main__":
    main()
