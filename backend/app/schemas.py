from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "student"

class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class LectureBase(BaseModel):
    title: str
    description: str
    date_time: datetime

class LectureCreate(LectureBase):
    teacher_id: int

class AssignmentBase(BaseModel):
    title: str
    description: str
    due_date: datetime

class AssignmentCreate(AssignmentBase):
    teacher_id: int

class NoticeBase(BaseModel):
    title: str
    content: str

class NoticeCreate(NoticeBase):
    posted_by: int
