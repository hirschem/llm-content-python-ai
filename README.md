# LLM Content Pipeline (Python)

A modular Python pipeline that ingests public web content, normalizes it into structured records, optionally filters/classifies items, summarizes content with an LLM into JSON, and generates a blog-ready Markdown post.

> This repository is a **sanitized demonstration** of a client-style system built for automated editorial workflows. It contains no proprietary client code, prompts, or source lists.

## What it does
1. **Ingest**: Reads items from an example RSS feed (pluggable ingestion layer)
2. **Normalize**: Converts raw items into a consistent schema
3. **Filter/Classify**: Applies basic tag rules (placeholder for more advanced logic)
4. **Summarize**: Produces structured JSON summaries (mock by default; OpenAI-compatible optional)
5. **Publish**: Generates a Markdown post with headings and bullet summaries

## Outputs
- `data/sample_output/normalized_items.json`
- `data/sample_output/summaries.json`
- `data/sample_output/final_post.md`

## Quickstart
### 1) Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### 2) Run the pipeline
```bash
python -m src.pipeline.run_pipeline
```

### 3) View output
Check `data/sample_output/` for JSON + Markdown artifacts.

## Notes on NDA Safety
This repo demonstrates **patterns** (interfaces, orchestration, schemas, structured output) rather than any client-specific configuration.
See `docs/NDA_SAFE_NOTES.md`.

## Tech
- Python 3.11+
- feedparser
- pydantic schemas
- dotenv config
