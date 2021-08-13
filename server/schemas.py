from pydantic import BaseModel

class Caption(BaseModel):
    id: int
    startTime: int
    caption: str
    videoId: str

    class Config:
        orm_mode = True

class Video(BaseModel):
    videoId: str
    videoTitle: str
    datePosted: str

    class Config:
        orm_mode = True