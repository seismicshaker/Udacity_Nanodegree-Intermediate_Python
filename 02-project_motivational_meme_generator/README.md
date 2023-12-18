# Udacity Project: Motivational Meme Generator

## Overview

The final project for Udacity's Intermediate Python Nanodegree is a "Meme Generator". This includes a Command-Line Interface (`meme.py`) and Flask application (`app.py`) to generate a dog meme with superimposed quote.

## Working Folder Structure

```bash
|-- _data
|-- fonts
|-- MemeEngine
    |-- MemeEngine.py
|-- QuoteEngine
    |-- FileIngestors.py
    |-- Ingestor.py
    |-- IngestorInterface.py
    |-- QuoteModel.py
|-- static
|-- templates
|-- tmp
```

## Working Modules

### QuoteEngine

The `QuoteEngine` module is responsible for ingesting files (.txt, .docx, .pdf, or .csv) that contain quotes. Further, the module distinguishes quote body and quote author.

### MemeEngine

The `MemeEngine` module is responsible for loading/manipulating images and superimposing a quote. Further, the module can save the meme to the local disk.

# Installation

## Installing Xpdf

Xpdf may not be installed on your local machine. If this is the case, you can install it using the open source XpdfReader utility. Here are some tips for installing xpdf on different operating systems:

For Mac, we suggest that you use Homebrew:
 - If you don't already have it, install use the command provided here to install Homebrew. After installing, read the last few lines that it outputs in your CLI—it may provide additional commands that you can run to add Homebrew to PATH.
 - Once Homebrew is installed, simply run `brew install xpdf` in the terminal.

 For Windows, you'll need to:
 - Download the Windows command-line tools from the xpdf website.
 - Unzip the files in a location of your choice.
 - Get the full file path to the folder named `bin32` (if you have a 32-bit machine) or `bin64` (if you have a 64-bit machine).
 - Add this path to the `Path` environment variable. This will allow you to use the xpdf command from the command line. If you've never done this before, check out this Stack Overflow post on how to add a folder to the **`Path`** environment variable.

For Linux, you can use Homebrew (as shown above for Mac) or `apt-get` to install (simply enter `sudo apt-get install -y xpdf` in your command line interface).

## Installing Python Dependencies

```bash
pip install -r requirements.txt
```

# Running the project

## Command-Line Interface

```bash
python meme.py -h       
usage: MemeGenerator [-h] [-p PATH] [-b BODY] [-a AUTHOR]

Dog meme generator with fun quotes.

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to image file
  -b BODY, --body BODY  Quote body to add to the image
  -a AUTHOR, --author AUTHOR
                        Quote author to add to the image
```

## Flask Application

```bash
python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open `http://127.0.0.1:5000` in a browser to interface with web app.
