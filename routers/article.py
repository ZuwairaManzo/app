from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine  
from models import Article

router = APIRouter(
    prefix="/articles",
    tags=["articles"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    return articles