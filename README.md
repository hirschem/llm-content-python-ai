# LLM Content Pipeline (Python)

NDA-safe example of an AI-powered content pipeline based on patterns used in a real client system.

## Overview

This project demonstrates a modular pipeline for ingesting, structuring, and generating content using AI.

It is a simplified, sanitized version of a larger real-world system built for automated editorial workflows. The full implementation cannot be shared due to NDA, but this repository reflects the core architecture, data flow, and design decisions.

The focus is on building predictable, structured pipelines around AI systems rather than relying on single-pass generation.

## What this demonstrates

- Structuring AI workflows into deterministic steps  
- Normalizing unstructured input into consistent schemas  
- Handling variability in AI-generated outputs  
- Separating ingestion, processing, and generation layers  
- Producing structured outputs (JSON + Markdown)  

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

    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    cp .env.example .env

### 2) Run the pipeline

    python -m src.pipeline.run_pipeline

### 3) View output

Check `data/sample_output/` for JSON and Markdown artifacts.

## NDA Notes

This repository is a sanitized demonstration of a client-style system.

It reflects:

- Workflow structure  
- Data processing patterns  
- AI integration approach  

It does not include:

- Client-specific prompts or logic  
- Proprietary data sources  
- Internal integrations  
- Production infrastructure  

## Tech Stack

- Python 3.11+  
- feedparser  
- pydantic  
- dotenv  

## Design Focus

- Breaking AI workflows into repeatable stages  
- Ensuring predictable output structure  
- Handling incomplete or inconsistent data  
- Maintaining clear boundaries between pipeline steps  

## Status

Reference implementation demonstrating system design and workflow structure. Not a full production system.
