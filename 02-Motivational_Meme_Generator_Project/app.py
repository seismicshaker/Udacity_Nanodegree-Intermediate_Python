import random
from os import walk
from os.path import join
from tempfile import NamedTemporaryFile

import requests
from flask import Flask, abort, redirect, render_template, request, url_for

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    # Parse all files in the quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # Find all images within the images images_path directory
    imgs = [
        join(root, f) for root, _, files in walk(images_path) for f in files
    ]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    # Select a random image from imgs array
    img = random.choice(imgs)
    # Select a random quote from the quotes array
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    tmp = NamedTemporaryFile(delete=False)

    # Save the image from the image_url form param to a temp local file.
    img = request.form.get("image_url")
    body = request.form.get("body")
    author = request.form.get("author")

    try:
        img_content = requests.get(img, stream=True, timeout=5).content
        # Use the meme object to generate a meme using this temp
        #    file and the body and author form paramaters.
        with open(tmp.name, "wb") as fin:
            fin.write(img_content)

        path = meme.make_meme(tmp.name, body, author)
    finally:
        # Remove the temporary saved image.
        tmp.close()

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(debug=False)
