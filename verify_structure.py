import os

def verify_structure():
    """Verify that the project structure is correct"""
    
    # Define expected directories
    expected_directories = [
        "backend",
        "backend/app",
        "backend/app/routes",
        "frontend",
        "frontend/src",
        "frontend/src/api",
        "frontend/src/components",
        "frontend/src/pages",
        "frontend/src/styles"
    ]
    
    # Define expected files
    expected_files = [
        # Backend files
        "backend/app/main.py",
        "backend/app/models.py",
        "backend/app/schemas.py",
        "backend/app/database.py",
        "backend/app/auth.py",
        "backend/app/routes/users.py",
        "backend/app/routes/lectures.py",
        "backend/app/routes/assignments.py",
        "backend/app/routes/notices.py",
        "backend/requirements.txt",
        
        # Frontend files
        "frontend/src/App.jsx",
        "frontend/src/main.jsx",
        "frontend/src/api/api.js",
        "frontend/src/components/Navbar.jsx",
        "frontend/src/components/Dashboard.jsx",
        "frontend/src/components/LectureList.jsx",
        "frontend/src/components/AssignmentList.jsx",
        "frontend/src/components/NoticeBoard.jsx",
        "frontend/src/pages/Login.jsx",
        "frontend/src/pages/Signup.jsx",
        "frontend/src/pages/Profile.jsx",
        "frontend/src/styles/tailwind.css",
        "frontend/package.json",
        "frontend/vite.config.js"
    ]
    
    print("Verifying project structure...")
    
    # Check directories
    missing_directories = []
    for directory in expected_directories:
        if not os.path.exists(directory):
            missing_directories.append(directory)
        else:
            print(f"✓ Found directory: {directory}")
    
    # Check files
    missing_files = []
    for file_path in expected_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"✓ Found file: {file_path}")
    
    # Report results
    print("\n" + "="*50)
    print("VERIFICATION RESULTS")
    print("="*50)
    
    if missing_directories:
        print(f"Missing directories ({len(missing_directories)}):")
        for directory in missing_directories:
            print(f"  - {directory}")
    else:
        print("✓ All directories present")
    
    if missing_files:
        print(f"Missing files ({len(missing_files)}):")
        for file_path in missing_files:
            print(f"  - {file_path}")
    else:
        print("✓ All files present")
    
    if not missing_directories and not missing_files:
        print("\n✓ Project structure verification PASSED")
        return True
    else:
        print("\n✗ Project structure verification FAILED")
        return False

if __name__ == "__main__":
    verify_structure()