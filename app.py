from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    wines = db.query(models.Wine).all()
    return templates.TemplateResponse("index.html", {"request": request, "wines": wines})

@app.post("/add")
def add_wine(
    name: str = Form(...),
    region: str = Form(...),
    year: int = Form(...),
    price: float = Form(...),
    db: Session = Depends(get_db)
):
    wine = models.Wine(name=name, region=region, year=year, price=price)
    db.add(wine)
    db.commit()
    return {"success": True}

