from sqlalchemy.orm import Session
from sqlalchemy import func
import database
import models

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
       db.close() 

async def get_title(videoId: str, db: Session):
    return db.query(models.Video).filter(models.Video.videoId == videoId).first()

async def search(phrase: str, db: Session):
    phrase_ws = phrase.replace(" ", "")
    primary_res = db.query(models.Caption).filter(models.Caption.caption.match(f"%{phrase_ws}%")).all()
    if len(primary_res):
        return primary_res
    return db.query(models.Caption).filter(func.lower(models.Caption.caption).contains(func.lower(phrase))).all()