"""
Quote model modeule for the QuoteModel class.
"""


class QuoteModel:
    """Quote Model Class for motivational quote objects."""

    def __init__(self, quote_body: str, quote_author: str) -> None:
        """
        Creates new motivational quote.

        input: quote_body -
            The motivational quote's body text.
        input quote_author -
            The motivational quote's author.
        """

        self.body = quote_body
        self.author = quote_author

    @property
    def __repr__(self):
        return f"{self.body} - {self.author}"

    def __str__(self):
        return f'"{self.body}" by {self.author}'
