from __future__ import annotations
from typing import List
from datetime import date
from src.llm.schemas import Summary

def generate_markdown(summaries: List[Summary], title: str = "Weekly Music & Culture Digest") -> str:
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"_Generated: {date.today().isoformat()}_")
    lines.append("")
    for s in summaries:
        tag_str = f" — **Tags:** {', '.join(s.tags)}" if s.tags else ""
        lines.append(f"## [{s.title}]({s.url}){tag_str}")
        lines.append("")
        lines.append(f"**TL;DR:** {s.one_sentence}")
        lines.append("")
        for b in s.bullets:
            lines.append(f"- {b}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"
