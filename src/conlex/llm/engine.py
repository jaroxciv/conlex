import os
from dotenv import load_dotenv
from openai import OpenAI
from loguru import logger

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def call_llm(prompt, model="gpt-4o", temperature=0.2):
    logger.debug(f"Calling LLM model={model}, temp={temperature}, prompt length={len(prompt)} chars")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    logger.info("LLM response received.")
    return response.choices[0].message.content
