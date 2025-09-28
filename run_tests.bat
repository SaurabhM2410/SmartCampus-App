@echo off
echo ==================================================
echo hackdemo - Project Testing Script
echo ==================================================

echo.
echo 1. Verifying project structure...
python verify_structure.py

echo.
echo 2. Checking backend dependencies...
cd backend
pip list | findstr -i "fastapi\|uvicorn\|sqlalchemy\|pydantic"
if %errorlevel% neq 0 (
    echo Warning: Some backend dependencies may not be installed
) else (
    echo ✓ Backend dependencies found
)

echo.
echo 3. Checking frontend dependencies...
cd ..\frontend
npm list --depth=0 | findstr -i "react\|vite\|axios"
if %errorlevel% neq 0 (
    echo Warning: Some frontend dependencies may not be installed
) else (
    echo ✓ Frontend dependencies found
)

echo.
echo 4. Running automated tests...
cd ..
echo Running frontend component tests...
echo Note: Frontend tests require Jest to be set up
echo Test files located in frontend/src/tests/
echo.
echo Running backend API tests...
cd backend
python test_backend.py
cd ..

echo.
echo 5. Testing backend server startup...
timeout /t 2 /nobreak >nul
echo To test the backend API:
echo    - Run: cd backend
echo    - Run: uvicorn app.main:app --reload
echo    - Visit: http://127.0.0.1:8000/docs

echo.
echo 6. Testing frontend server startup...
echo To test the frontend:
echo    - Run: cd frontend
echo    - Run: npm run dev
echo    - Visit: http://localhost:5173

echo.
echo ==================================================
echo Testing complete. Manual testing instructions above.
echo ==================================================
pause