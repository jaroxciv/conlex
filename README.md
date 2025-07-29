# conlex

A modular, production-grade Python pipeline for **AI-powered contract analysis** using large language models (LLMs) — optimized for legal, business, and negotiation insight.

## 🚀 Features

* **Automated analysis** of legal contracts (e.g., CTO Equity Agreement, Shareholder Agreement)
* **Self-reflexive LLM pipeline:** analysis → critique → judge → improve
* **Markdown output:** Clear, professional results with risk matrices and actionable questions
* **Chunked input:** Handles long contracts safely (avoids LLM token limits)
* **Flexible and extensible:** Modern code structure, easily add more models/providers

## 🛠️ Quick Start

1. **Clone the repo**

   ```sh
   git clone https://github.com/jaroxciv/conlex.git
   cd conlex
   ```

2. **Install dependencies**

   ```sh
   uv pip install -e .
   ```

3. **Set your OpenAI API key**

   * Copy `.env.example` to `.env` and add your `OPENAI_API_KEY`
   * Or create `.env`:

     ```
     OPENAI_API_KEY=your-openai-key-here
     ```

4. **Add contract files to the `data/` folder**

   * Example: `data/equity.docx`, `data/sha.docx`

5. **Run the analysis**

   ```sh
   uv run scripts/analyse_contracts.py equity.docx sha.docx --synthesize
   ```

   * Outputs will be saved to `outputs/` as Markdown files.

## 🧩 Project Structure

```
src/conlex/         # Main package code
    io/             # Input/output utilities (e.g., DOCX loader)
    llm/            # LLM engine and prompts
    utils/          # Helpers (e.g., text chunking)
scripts/            # CLI entrypoints
data/               # Input contracts (not tracked)
outputs/            # Results (.md files)
```

## 🤖 LLM Pipeline

1. **Chunk contracts for LLM safety**
2. **LLM produces structured Markdown analysis**
3. **Self-reflexion steps:**

   * Critic (find flaws)
   * Judge (score and summarize)
   * Improver (final, improved Markdown report)
4. **Optionally synthesize analyses for multi-document review**

## 📄 Example Output

* **Benefits**
* **Concerns**
* **Questions**
* **Risk Matrix**
* **Summary/Advice**

All sections formatted in Markdown for easy review or sharing.

## 🙌 Contributing

PRs, suggestions, and issue reports welcome!
Let’s build the future of AI-powered legal analysis together.

> **For legal or business advice, always consult a qualified human lawyer. This project is for research and augmentation, not a substitute for professional counsel.**
