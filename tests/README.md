# Unit Tests for Fortnite Shop

This directory contains unit tests for the Fortnite Shop application using pytest.

## Running the Tests

1. Install the required dependencies:
```bash
pip install -r ../requirements.txt
```

2. Run the tests from the project root directory:
```bash
pytest
```

3. To run tests with more detailed output:
```bash
pytest -v
```

4. To run specific test files:
```bash
pytest tests/test_app.py
```

5. To generate a test coverage report:
```bash
pip install pytest-cov
pytest --cov=app tests/
```

## Test Structure

- `conftest.py`: Contains shared fixtures used across test files
- `test_app.py`: Tests for Flask routes and API endpoints, cart functionality, and data validation

## Writing New Tests

When adding new features to the app, please add appropriate tests to maintain coverage. 