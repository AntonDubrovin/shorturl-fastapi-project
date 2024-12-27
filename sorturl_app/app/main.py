from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/shorten/", response_model=schemas.URLResponse)
def shorten_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    return crud.create_short_url(db, url)


@app.get("/{short_id}")
def redirect_url(short_id: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_short_id(db, short_id)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": db_url.full_url}


@app.get("/stats/{short_id}", response_model=schemas.URLResponse)
def get_url_stats(short_id: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_stats(db, short_id)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url
