from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
SAMPLE_INPUT = DATA_DIR / "sample_input" / "sample_feed.xml"
SAMPLE_OUTPUT_DIR = DATA_DIR / "sample_output"

@dataclass(frozen=True)
class PipelineConfig:
    input_feed_path: Path = SAMPLE_INPUT
    output_dir: Path = SAMPLE_OUTPUT_DIR
    use_mock_summarizer: bool = os.getenv("USE_MOCK_SUMMARIZER", "true").lower() in {"1", "true", "yes"}
