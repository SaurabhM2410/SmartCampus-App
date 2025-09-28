from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter()

# Get all assignments
@router.get("/", response_model=List[schemas.AssignmentBase])
def get_assignments(db: Session = Depends(database.get_db)):
    return db.query(models.Assignment).all()

# Create assignment
@router.post("/", response_model=schemas.AssignmentBase)
def create_assignment(assignment: schemas.AssignmentCreate, db: Session = Depends(database.get_db)):
    db_assignment = models.Assignment(
        title=assignment.title,
        description=assignment.description,
        due_date=assignment.due_date,
        teacher_id=assignment.teacher_id
    )
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

# Get assignment by ID
@router.get("/{assignment_id}", response_model=schemas.AssignmentBase)
def get_assignment(assignment_id: int, db: Session = Depends(database.get_db)):
    assignment = db.query(models.Assignment).filter(models.Assignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment
