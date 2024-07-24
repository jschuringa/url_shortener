from sqlalchemy.orm import Session

from . import models

def create_url(db: Session, target: str, short: str) -> models.URL:
    m = models.URL(
        target=target, short=short
    )
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

def get_url(db: Session, short: str) -> models.URL:
    return (db.query(models.URL).filter(models.URL.short==short).first())