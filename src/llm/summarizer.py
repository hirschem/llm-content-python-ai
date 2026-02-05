from __future__ import annotations
from typing import List, Protocol
from src.llm.schemas import NormalizedItem, Summary

class Summarizer(Protocol):
    def summarize(self, items: List[NormalizedItem]) -> List[Summary]:
        ...

class MockSummarizer:
    def summarize(self, items: List[NormalizedItem]) -> List[Summary]:
        out: List[Summary] = []
        for it in items:
            text = (it.text or "").strip()
            one = text.split(".")[0].strip() if text else "Summary placeholder for demo data."
            bullets = []
            if text:
                # naive bullet split
                for part in text.replace("\n", " ").split(".")[:3]:
                    part = part.strip()
                    if part:
                        bullets.append(part if part.endswith(".") else part + ".")
            if not bullets:
                bullets = ["Demo bullet point 1.", "Demo bullet point 2."]
            out.append(Summary(title=it.title, url=it.url, one_sentence=one if one else it.title, bullets=bullets, tags=it.tags))
        return out

# Optional: wire up a real OpenAI summarizer later.
# Keep this interface stable; swap the implementation in `run_pipeline.py`.
