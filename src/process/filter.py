from __future__ import annotations
from typing import List
from src.llm.schemas import NormalizedItem

# Generic example rules (replace with your own domain logic)
TAG_RULES = {
    "hip-hop": ["hip hop", "rap", "mc"],
    "indie": ["indie", "alt", "alternative"],
    "electronic": ["electronic", "edm", "synth"],
}

def apply_filter(items: List[NormalizedItem]) -> List[NormalizedItem]:
    kept: List[NormalizedItem] = []
    for it in items:
        hay = f"{it.title} {it.text}".lower()
        tags = []
        for tag, keys in TAG_RULES.items():
            if any(k in hay for k in keys):
                tags.append(tag)

        # Example policy: keep if any tag matched, otherwise drop
        if tags:
            it.tags = tags
            kept.append(it)
    return kept
