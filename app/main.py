import validators
import random
import string

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import requests, models
from .db import SessionLocal, engine
from .repository import get_url, create_url

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# just breaking this out for test coverage
def get_short() -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


@app.post("/url", response_model=requests.Redirect)
def new_url(url: requests.URL, db: Session = Depends(get_db)):
    if not validators.url(url.target):
        raise HTTPException(status_code=400, detail="invalid target url")
    # add retry logic here if short already exists - faster to attempt to insert and get unique key error than 
    # to check beforehand every time
    short = get_short()
    u = create_url(db, url.target, short)

    return requests.Redirect(short=short, target=url.target)

@app.get("/{short}")
def fwd(short: str, request: Request, db: Session = Depends(get_db)):
    u = get_url(db, short)
    if u:
        return RedirectResponse(u.target)
    else:
        raise HTTPException(status_code=404, detail=f"url {short} not found")

