from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional

class RawItem(BaseModel):
    title: str
    link: str
    published: Optional[str] = None
    summary: Optional[str] = None

class NormalizedItem(BaseModel):
    title: str
    url: str
    published: Optional[str] = None
    text: str = Field(default="")
    tags: List[str] = Field(default_factory=list)

class Summary(BaseModel):
    title: str
    url: str
    one_sentence: str
    bullets: List[str]
    tags: List[str] = Field(default_factory=list)
