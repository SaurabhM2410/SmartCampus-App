from fastapi import FastAPI
from .database import Base, engine, get_db
from .routes import users, lectures, assignments, notices

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Campus API")

# include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(lectures.router, prefix="/lectures", tags=["Lectures"])
app.include_router(assignments.router, prefix="/assignments", tags=["Assignments"])
app.include_router(notices.router, prefix="/notices", tags=["Notices"])
