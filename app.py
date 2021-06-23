from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/actors/", response_model=List[schemas.Actor])
def read_actors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    actors = crud.get_actors(db, skip=skip, limit=limit)
    return actors