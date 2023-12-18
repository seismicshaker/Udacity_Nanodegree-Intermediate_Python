import argparse
import os
import random

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote"""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="MemeGenerator", description="Dog meme generator with fun quotes."
    )
    parser.add_argument("-p", "--path", help="Path to image file", type=str)
    parser.add_argument(
        "-b", "--body", help="Quote body to add to the image", type=str
    )
    parser.add_argument(
        "-a", "--author", help="Quote author to add to the image", type=str
    )
    args = parser.parse_args()
    print("Open meme here,", generate_meme(args.path, args.body, args.author))
