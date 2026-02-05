from __future__ import annotations
from typing import List
from src.llm.schemas import RawItem, NormalizedItem

def normalize(items: List[RawItem]) -> List[NormalizedItem]:
    out: List[NormalizedItem] = []
    for it in items:
        text = (it.summary or "").strip()
        out.append(
            NormalizedItem(
                title=it.title,
                url=it.link,
                published=it.published,
                text=text,
                tags=[],
            )
        )
    return out
