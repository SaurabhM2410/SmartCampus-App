from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter()

# Get all lectures
@router.get("/", response_model=List[schemas.LectureBase])
def get_lectures(db: Session = Depends(database.get_db)):
    return db.query(models.Lecture).all()

# Create lecture
@router.post("/", response_model=schemas.LectureBase)
def create_lecture(lecture: schemas.LectureCreate, db: Session = Depends(database.get_db)):
    db_lecture = models.Lecture(
        title=lecture.title,
        description=lecture.description,
        date_time=lecture.date_time,
        teacher_id=lecture.teacher_id
    )
    db.add(db_lecture)
    db.commit()
    db.refresh(db_lecture)
    return db_lecture

# Get lecture by ID
@router.get("/{lecture_id}", response_model=schemas.LectureBase)
def get_lecture(lecture_id: int, db: Session = Depends(database.get_db)):
    lecture = db.query(models.Lecture).filter(models.Lecture.id == lecture_id).first()
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return lecture
