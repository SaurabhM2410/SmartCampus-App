from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter()

# Get all notices
@router.get("/", response_model=List[schemas.NoticeBase])
def get_notices(db: Session = Depends(database.get_db)):
    return db.query(models.Notice).all()

# Create notice
@router.post("/", response_model=schemas.NoticeBase)
def create_notice(notice: schemas.NoticeCreate, db: Session = Depends(database.get_db)):
    db_notice = models.Notice(
        title=notice.title,
        content=notice.content,
        posted_by=notice.posted_by
    )
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

# Get notice by ID
@router.get("/{notice_id}", response_model=schemas.NoticeBase)
def get_notice(notice_id: int, db: Session = Depends(database.get_db)):
    notice = db.query(models.Notice).filter(models.Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    return notice
