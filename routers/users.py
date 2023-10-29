from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user