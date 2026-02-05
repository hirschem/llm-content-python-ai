from __future__ import annotations

import json
from pathlib import Path
from dotenv import load_dotenv

from src.pipeline.config import PipelineConfig
from src.utils.logging import get_logger
from src.ingest.rss_ingest import RSSFileIngestor
from src.process.normalize import normalize
from src.process.filter import apply_filter
from src.llm.summarizer import MockSummarizer
from src.publish.markdown_generator import generate_markdown

logger = get_logger("pipeline")

def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False))

def main() -> None:
    load_dotenv()
    cfg = PipelineConfig()
    cfg.output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Ingesting RSS items…")
    raw = RSSFileIngestor(cfg.input_feed_path).ingest()

    logger.info("Normalizing…")
    normalized = normalize(raw)
    write_json(cfg.output_dir / "normalized_items.json", [x.model_dump() for x in normalized])

    logger.info("Filtering/classifying…")
    kept = apply_filter(normalized)

    logger.info("Summarizing…")
    # Swap this with a real summarizer when ready.
    summarizer = MockSummarizer()
    summaries = summarizer.summarize(kept)
    write_json(cfg.output_dir / "summaries.json", [x.model_dump() for x in summaries])

    logger.info("Publishing Markdown…")
    md = generate_markdown(summaries)
    (cfg.output_dir / "final_post.md").write_text(md, encoding="utf-8")

    logger.info("Done. See data/sample_output/")

if __name__ == "__main__":
    main()
