def chunk_text(text, max_words=2000):
    # Split text into manageable chunks for the LLM (by words)
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i+max_words])
