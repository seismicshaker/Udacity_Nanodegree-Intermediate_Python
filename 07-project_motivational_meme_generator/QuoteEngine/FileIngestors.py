"""
Collection of File Ingestors built from the IngestorInterface class.

Includes ingestors for the following files:
    (1) txt - TextIngestor
    (2) docx - DocxIngestor
    (3) pdf - PDFIngestor
    (4) csv - CSVIngestor
"""

import subprocess
from tempfile import NamedTemporaryFile

import docx
import pandas as pd

from .IngestorInterface import IngesterInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngesterInterface):
    """Ingest CSV files using the native file library."""

    file_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str):
        """
        Parse through file to extract quotes, body and author, and return list
        of QuoteModel onjects.

        input: path -
            Path location of quote csv file
        output: quotes -
            List of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(f"{path} cannot be ingested by {cls.__name__}.")

        try:
            quotes = []
            csv = pd.read_csv(path)
            # parce csv file
            for _, row in csv.iterrows():
                quote = QuoteModel(row.body, row.author)

                quotes.append(quote)

            return quotes

        except FileNotFoundError as error_out:
            print(error_out)


class DocxIngestor(IngesterInterface):
    """Ingest DOCX files using the native file library."""

    file_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str):
        """
        Parse through file to extract quotes, body and author, and return list
        of QuoteModel onjects.

        input: path -
            Path location of quote docx file
        output: quotes -
            List of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(f"{path} cannot be ingested by {cls.__name__}.")

        try:
            quotes = []
            docx_file = docx.Document(path)

            # parse docx file
            for line in docx_file.paragraphs:
                if line.text != "":
                    [body, author] = line.text.split(" - ")
                    body = body.strip('"')
                    author = author.strip("\n")

                    # create QuoteModel
                    quote = QuoteModel(body, author)

                    quotes.append(quote)

            return quotes

        except FileNotFoundError as error_out:
            print(error_out)


class PDFIngestor(IngesterInterface):
    """Ingest PDF files using the native file library."""

    file_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str):
        """
        Parse through file to extract quotes, body and author, and return list
        of QuoteModel onjects.

        input: path -
            Path location of quote pdf file
        output: quotes -
            List of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(f"{path} cannot be ingested by {cls.__name__}.")

        tmp = NamedTemporaryFile(delete=False)
        try:
            # call pdftotext via subprocess
            subprocess.call(
                ["pdftotext", "-layout", path, tmp.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            with open(tmp.name, "r", encoding="utf-8-sig") as fin:
                quotes = []
                # parse text file
                for line in fin.readlines():
                    if len(line) > 1:
                        [body, author] = line.split(" - ")
                        body = body.strip('"')
                        author = author.strip("\n")
                        # create QuoteModel
                        quote = QuoteModel(body, author)

                        quotes.append(quote)

            return quotes

        except FileNotFoundError as error_out:
            print(error_out)

        finally:
            tmp.close()


class TextIngestor(IngesterInterface):
    """Ingest TXT files using the native file library."""

    file_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str):
        """
        Parse through file to extract quotes, body and author, and return list
        of QuoteModel onjects.

        input: path -
            Path location of quote txt file
        output: quotes -
            List of QuoteModel objects
        """
        if not cls.can_ingest(path):
            raise Exception(f"{path} cannot be ingested by {cls.__name__}.")

        try:
            with open(path, "r", encoding="utf-8-sig") as fin:
                quotes = []
                # parse text file
                for line in fin.readlines():
                    if len(line) > 0:
                        [body, author] = line.split(" - ")
                        body = body.strip('"')
                        author = author.strip("\n")
                        # create QuoteModel
                        quote = QuoteModel(body, author)

                        quotes.append(quote)

            return quotes

        except FileNotFoundError as error_out:
            print(error_out)
