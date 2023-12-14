"""
Ingester Interface modeule for the abstract class, IngesterInterface.
"""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngesterInterface(ABC):
    """Skeletal ingester classes."""

    file_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Method to check whether quote file is ingestable.

        input: path
            Path location of quote file
        output:
            boolean statement on whether file extention is ingestable
        """
        ext = path.split(".")[-1]
        return ext in cls.file_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Abtractmethod for parsing the file content (i.e., splitting each row)
        and outputting it to a Quote object.
        """
        pass
