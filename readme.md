# URL Shortener
A simple url shortener written using fastapi, sqlalchemy, and sqlite

## Endpoints
`POST /url`

Request: `{target: "validurl"}` e

x: `{target: "https://www.google.com"}`

Response: `{target: "validurl", short:"shortenedurlcode"}` 

ex: `{target: "https://www.google.com", short:"PSck3o"}`

`GET /{short}`

Request: query param of short, ex: `127.0.0.1:8000/PSck3o`

Response: if short exists, redirect. otherwise return not found.

## Setup

Typical venv setup - 

`python3 -m venv venv`

`source venv/bin/activate`

`python -m pip install -r requirements.txt`

## Running

`uvicorn app.main:app --reload`

## Running tests
`pytest tests/`
