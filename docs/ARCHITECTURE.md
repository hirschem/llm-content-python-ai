# Architecture

## Pipeline stages
Ingest → Normalize → Filter/Classify → Summarize → Publish (Markdown)

## Data flow
- Ingest returns `RawItem[]`
- Normalize converts to `NormalizedItem[]`
- Filter returns `NormalizedItem[]` (subset + tags)
- Summarize returns `Summary[]` in structured JSON
- Publish renders Markdown

## Design goals
- Pluggable ingestion sources
- Deterministic intermediate artifacts (JSON written between stages)
- Structured output schemas for predictable downstream behavior
- Clear separation of concerns for testing + maintenance

## Modules
- `src/ingest/*` : ingestion adapters (RSS demo; others can be added)
- `src/process/*`: normalization + filtering
- `src/llm/*`    : summarizer interface + schemas
- `src/publish/*`: Markdown generation
- `src/pipeline/*`: orchestration + config
