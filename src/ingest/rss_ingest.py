from __future__ import annotations
from typing import List
from pathlib import Path
import feedparser

from src.ingest.base import Ingestor
from src.llm.schemas import RawItem

class RSSFileIngestor(Ingestor):
    def __init__(self, feed_path: Path):
        self.feed_path = feed_path

    def ingest(self) -> List[RawItem]:
        parsed = feedparser.parse(str(self.feed_path))
        items: List[RawItem] = []
        for entry in parsed.entries:
            items.append(
                RawItem(
                    title=getattr(entry, "title", "").strip(),
                    link=getattr(entry, "link", "").strip(),
                    published=getattr(entry, "published", None),
                    summary=getattr(entry, "summary", None),
                )
            )
        return items
