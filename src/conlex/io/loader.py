# src/io/loader.py
from docx import Document
from loguru import logger

def load_contract(path):
    logger.info(f"Loading contract from: {path}")
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
