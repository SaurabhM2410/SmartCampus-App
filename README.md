<<<<<<< HEAD
# Smart Campus.com - All-in-One College Management System

## Overview
Smart Campus.com is a hackathon MVP that centralizes lectures, assignments, notices, and profiles for students, teachers, and administrators.

## Tech Stack
- Frontend: React.js + Tailwind CSS
- Backend: FastAPI
- Database: SQLite (or Firebase Firestore for real-time updates)
- Authentication: JWT
- Hosting: Vercel / Firebase Hosting

## UI Implementation

The frontend UI has been completely redesigned with a modern, responsive design following these principles:

- **Clean & Professional**: Minimal design with ample whitespace
- **Responsive**: Works on mobile, tablet, and desktop devices
- **Role-Based**: Different interfaces for Students, Faculty, and Admin
- **Consistent**: Unified color scheme and component design

### Color Palette
- Primary: `#1E3A8A` (Deep Blue)
- Secondary: `#2563EB` (Bright Blue)
- Accent: `#22C55E` (Green for success)
- Neutral: White, Gray (`#F9FAFB`, `#6B7280`)

For detailed UI documentation, see [frontend/UI_README.md](frontend/UI_README.md)

## Setup Instructions

### Backend
1. Navigate to backend folder:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
uvicorn app.main:app --reload
```

4. Access the API documentation at: http://127.0.0.1:8000/docs

### Frontend
1. Navigate to frontend folder:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Install icon library:
```bash
npm install lucide-react
```

4. Run the development server:
```bash
npm run dev
```

5. Access the application at: http://localhost:5173

## UI Fix for Styling Issues

If the web page appears without proper UI styling and animations:

### Automated Fix Options:
1. **Batch Script** (Windows Command Prompt):
   ```bash
   cd frontend
   fix_tailwind.bat
   ```

2. **PowerShell Script** (Windows PowerShell):
   ```bash
   cd frontend
   .\fix_tailwind.ps1
   ```

### Manual Fix:
If the automated scripts don't work, follow the manual steps in `frontend/MANUAL_FIX_STEPS.md`.

### Common Issues:
1. Make sure Node.js is installed and accessible from your terminal
2. Check that all file paths are correct
3. Ensure there are no syntax errors in the configuration files

## Testing

### Automated Testing
Run the verification script to check project structure:
```bash
python verify_structure.py
```

### Manual Testing
1. Start both backend and frontend servers as described in Setup Instructions
2. Open your browser and navigate to http://localhost:5173
3. Test user registration and login functionality
4. Explore the dashboard, lecture list, assignment list, and notice board
5. Test profile management features

### API Testing
Use the interactive documentation at http://127.0.0.1:8000/docs to test all API endpoints:
- User signup and login
- Lecture management
- Assignment management
- Notice management

## Project Structure
- `backend/` - FastAPI backend with SQLite database
- `frontend/` - React.js frontend with Tailwind CSS
=======
# SmartCampus-App
SmartCampus: An AI-powered College Management System
>>>>>>> da27dfd345efb6c8aebc4e2fa0f5e4c84870c20f
