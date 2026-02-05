from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from src.llm.schemas import RawItem

class Ingestor(ABC):
    @abstractmethod
    def ingest(self) -> List[RawItem]:
        raise NotImplementedError
