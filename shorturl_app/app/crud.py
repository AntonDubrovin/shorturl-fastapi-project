import secrets
from sqlalchemy.orm import Session
from app import models, schemas


def create_short_url(db: Session, url: schemas.URLBase):
    short_url = secrets.token_urlsafe(6)
    db_url = models.URL(full_url=url.full_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_url_by_short_id(db: Session, short_id: str):
    return db.query(models.URL).filter(models.URL.short_url == short_id).first()


def get_url_stats(db: Session, short_id: str):
    return db.query(models.URL).filter(models.URL.short_url == short_id).first()
