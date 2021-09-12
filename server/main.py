import fastapi
import sqlalchemy.orm as orm
import services
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI(docs_url=None)

origins = [
    "http://localhost:3000",
    "https://wavefoogle.com",
    "http://wavefoogle.com"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/search")
async def search(search: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.search(search, db)

@app.get("/api/lucky")
async def search(search: str, db: orm.Session = fastapi.Depends(services.get_db)):
    return await services.lucky(search, db)