import fastapi
import sqlalchemy.orm as orm
import services
import schemas

from typing import List
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/video_title")
async def test_video(videoId: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.get_title(videoId, db)

@app.get("/api/search")
async def search(search: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.search(search, db)