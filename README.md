# Image Searcher
Image Searcher is image search service connector.
Currently, following service is supported.
 * Bing Image Search

## Requirement
 * Python 3.8

## Installation
The following commands install requirements library.
```bash
pip install -r requirements.txt
poetry install
```
## Preparation
Set following environment variable.

`BingAPIKey`: API key for using Bing Image Search

## How to run server
The following commands run server.
```bash
poetry run python app/main.py
```
