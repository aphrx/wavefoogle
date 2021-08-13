from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
import database as db

class Caption(db.Base):
    __tablename__ = "transcript"

    id = Column(Integer, primary_key=True)
    startTime = Column(Integer)
    caption = Column(String)
    videoId = Column(String)

class Video(db.Base):
    __tablename__ = "video"

    videoId = Column(String, primary_key=True)
    videoTitle = Column(String)
    datePosted = Column(DateTime)