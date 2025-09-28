# Smart Campus.com - Testing Guide

## Overview

This guide provides detailed instructions on how to run automated tests for Smart Campus.com. The system includes both frontend and backend components, each with their own testing frameworks and procedures.

## Prerequisites

Before running tests, ensure you have the following installed:
- Python 3.8+
- Node.js 14+
- npm 6+
- Required Python packages (from `backend/requirements.txt`)
- Required Node packages (from `frontend/package.json`)

## Frontend Testing

### Test Framework
The frontend uses Jest with React Testing Library for component testing.

### Test Structure
```
frontend/
└── src/
    └── tests/
        ├── Dashboard.test.jsx
        ├── CalendarView.test.jsx
        ├── MessagesView.test.jsx
        ├── ResourcesView.test.jsx
        ├── GradesView.test.jsx
        ├── ProfileView.test.jsx
        ├── SettingsView.test.jsx
        ├── HelpView.test.jsx
        └── testRunner.js
```

### Running Frontend Tests

#### 1. Run All Tests
```bash
cd frontend
npm test
```

#### 2. Run Specific Component Tests
```bash
cd frontend
node src/tests/testRunner.js --component Dashboard
```

#### 3. Run Tests with Verbose Output
```bash
cd frontend
npm test -- --verbose
```

#### 4. Run Tests in Watch Mode
```bash
cd frontend
npm test -- --watch
```

### Test Coverage
The frontend tests cover:
- Component rendering
- User interactions
- State management
- Props validation
- Event handling
- API integration points

## Backend Testing

### Test Framework
The backend uses Python's unittest framework with FastAPI TestClient.

### Test Structure
```
backend/
├── test_backend.py
└── app/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── auth.py
    ├── utils.py
    └── routes/
        ├── users.py
        ├── lectures.py
        ├── assignments.py
        └── notices.py
```

### Running Backend Tests

#### 1. Run All Backend Tests
```bash
cd backend
python test_backend.py
```

#### 2. Run Specific Test Class
```bash
cd backend
python -m unittest test_backend.TestUsersAPI
```

#### 3. Run Specific Test Method
```bash
cd backend
python -m unittest test_backend.TestUsersAPI.test_read_users
```

#### 4. Run Tests with Verbose Output
```bash
cd backend
python test_backend.py -v
```

### Test Coverage
The backend tests cover:
- API endpoint responses
- Database operations
- Data validation
- Error handling
- Authentication flows
- Business logic

## Integrated Testing

### Running All Tests Together

#### 1. Using the Main Test Script
```bash
python test_project.py
```

This script will:
- Run automated frontend and backend tests
- Start both servers
- Test API connectivity
- Provide a comprehensive test summary

#### 2. Using the Batch Script (Windows)
```bash
run_tests.bat
```

This script will:
- Verify project structure
- Check dependencies
- Run automated tests
- Provide manual testing instructions

## Continuous Integration

### GitHub Actions Workflow
To set up CI/CD, create a `.github/workflows/test.yml` file:

```yaml
name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install backend dependencies
      run: |
        cd backend
        pip install -r requirements.txt
    - name: Run backend tests
      run: |
        cd backend
        python test_backend.py
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: 14
    - name: Install frontend dependencies
      run: |
        cd frontend
        npm install
    - name: Run frontend tests
      run: |
        cd frontend
        npm test
```

## Test Results Interpretation

### Success Indicators
- ✓ Test passed
- All tests completed without errors
- Expected status codes received
- Correct data returned from APIs
- Components render without errors

### Failure Indicators
- ❌ Test failed
- Unexpected status codes
- Missing or incorrect data
- Component rendering errors
- Timeout errors
- Connection errors

### Common Issues and Solutions

#### 1. Dependency Issues
**Problem**: Missing dependencies
**Solution**: 
```bash
# For backend
cd backend
pip install -r requirements.txt

# For frontend
cd frontend
npm install
```

#### 2. Database Connection Issues
**Problem**: Tests fail due to database connection
**Solution**: 
- Ensure SQLite is available
- Check database file permissions
- Verify database connection string

#### 3. Port Conflicts
**Problem**: Tests fail due to port conflicts
**Solution**:
- Stop other running servers
- Change test port numbers
- Use different host addresses

#### 4. Timeout Issues
**Problem**: Tests timeout
**Solution**:
- Increase timeout values
- Optimize test code
- Run tests in smaller batches

## Performance Testing

### Load Testing
To perform load testing on the backend API:

1. Install locust:
```bash
pip install locust
```

2. Create a `locustfile.py`:
```python
from locust import HttpUser, task, between

class SmartCampusUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_users(self):
        self.client.get("/users/")
    
    @task
    def get_lectures(self):
        self.client.get("/lectures/")
```

3. Run load test:
```bash
locust -f locustfile.py
```

### Browser Performance Testing
To test frontend performance:

1. Use Lighthouse in Chrome DevTools
2. Run automated performance tests with Puppeteer
3. Monitor bundle sizes with webpack-bundle-analyzer

## Security Testing

### API Security Testing
1. Test authentication endpoints
2. Verify authorization levels
3. Check for SQL injection vulnerabilities
4. Validate input sanitization

### Frontend Security Testing
1. Check for XSS vulnerabilities
2. Verify CSRF protection
3. Test secure cookie settings
4. Validate form input validation

## Accessibility Testing

### Automated Accessibility Testing
1. Use axe-core with Jest for React components
2. Integrate pa11y for end-to-end accessibility testing
3. Test with screen readers
4. Verify keyboard navigation

## Test Maintenance

### Updating Tests
When modifying components or APIs:
1. Update corresponding test files
2. Run affected tests to verify changes
3. Update test documentation
4. Ensure backward compatibility

### Adding New Tests
When adding new features:
1. Create corresponding test files
2. Write comprehensive test cases
3. Integrate with test runner
4. Update test documentation

## Reporting

### Test Reports
The testing framework generates:
- Console output with pass/fail status
- Detailed error messages
- Performance metrics
- Coverage reports

### Test Coverage Reports
To generate coverage reports:
```bash
# For frontend (requires Jest coverage setup)
cd frontend
npm test -- --coverage

# For backend
cd backend
coverage run test_backend.py
coverage report
```

## Best Practices

### Test Writing
1. Write isolated tests that don't depend on each other
2. Use descriptive test names
3. Test both positive and negative cases
4. Mock external dependencies
5. Keep tests fast and focused

### Test Organization
1. Group related tests in the same file
2. Use consistent naming conventions
3. Maintain clear folder structure
4. Document complex test scenarios

### Test Execution
1. Run tests frequently during development
2. Use CI/CD for automated testing
3. Monitor test performance
4. Address flaky tests promptly

## Conclusion

Smart Campus.com includes a comprehensive testing framework that ensures code quality and system reliability. By following this guide, you can effectively run and maintain tests for both frontend and backend components.

Regular testing helps catch issues early, ensures feature stability, and provides confidence in deployments. The testing framework is designed to be extensible and maintainable for future development.