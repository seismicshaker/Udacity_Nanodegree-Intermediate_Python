"""
Main ingestor to match file extentions with file ingestor.
"""


from .FileIngestors import CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor
from .IngestorInterface import IngesterInterface


class Ingestor(IngesterInterface):
    """
    Combined ingestor class.
    """

    ingestors = [TextIngestor, DocxIngestor, PDFIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str):
        """
        Iterate through file ingestor parse methods to match file with apt
        ingestor.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
