import unittest
import sys
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Create a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the test client
client = TestClient(app)

class TestUsersAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create tables in the test database
        Base.metadata.create_all(bind=engine)
    
    @classmethod
    def tearDownClass(cls):
        # Drop tables after tests
        Base.metadata.drop_all(bind=engine)
        # Remove test database file
        if os.path.exists("test.db"):
            os.remove("test.db")
    
    def test_read_users(self):
        response = client.get("/users/")
        self.assertEqual(response.status_code, 200)
    
    def test_create_user(self):
        user_data = {
            "name": "Test User",
            "email": "test@example.com",
            "role": "student"
        }
        response = client.post("/users/", json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Test User")
    
    def test_read_user(self):
        # First create a user
        user_data = {
            "name": "Test User 2",
            "email": "test2@example.com",
            "role": "faculty"
        }
        create_response = client.post("/users/", json=user_data)
        user_id = create_response.json()["id"]
        
        # Then read the user
        response = client.get(f"/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Test User 2")

class TestLecturesAPI(unittest.TestCase):
    def test_read_lectures(self):
        response = client.get("/lectures/")
        self.assertEqual(response.status_code, 200)
    
    def test_create_lecture(self):
        lecture_data = {
            "title": "Test Lecture",
            "description": "This is a test lecture",
            "instructor": "Test Instructor",
            "duration": 60
        }
        response = client.post("/lectures/", json=lecture_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test Lecture")

class TestAssignmentsAPI(unittest.TestCase):
    def test_read_assignments(self):
        response = client.get("/assignments/")
        self.assertEqual(response.status_code, 200)
    
    def test_create_assignment(self):
        assignment_data = {
            "title": "Test Assignment",
            "description": "This is a test assignment",
            "due_date": "2025-12-31",
            "course": "Test Course"
        }
        response = client.post("/assignments/", json=assignment_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test Assignment")

class TestNoticesAPI(unittest.TestCase):
    def test_read_notices(self):
        response = client.get("/notices/")
        self.assertEqual(response.status_code, 200)
    
    def test_create_notice(self):
        notice_data = {
            "title": "Test Notice",
            "content": "This is a test notice",
            "author": "Test Author",
            "priority": "medium"
        }
        response = client.post("/notices/", json=notice_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test Notice")

class TestMainAPI(unittest.TestCase):
    def test_read_root(self):
        response = client.get("/")
        # The root endpoint might not exist, so we're checking for 404
        self.assertIn(response.status_code, [200, 404])
    
    def test_api_docs(self):
        response = client.get("/docs")
        self.assertEqual(response.status_code, 200)
    
    def test_api_redoc(self):
        response = client.get("/redoc")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)