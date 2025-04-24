# Fortnite Shop Application

A web application that simulates a Fortnite item shop with a shopping cart functionality.

## Prerequisites

- Python 3.12 or higher
- Google Chrome browser
- ChromeDriver (automatically managed by undetected-chromedriver)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd software_testing
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Running Tests

The project includes both unit tests and functional tests.

### Unit Tests
To run unit tests:
```bash
pytest tests/test_app.py -v
```

### Functional Tests
To run functional tests (requires the Flask server to be running):

1. First, make sure the Flask application is running in a separate terminal
2. Then run:
```bash
pytest tests/test_functional_blaze.py -v
```

## Blazemeter Plugin installation

Add this plugin on your google chrome - 

https://chromewebstore.google.com/detail/mbopgmdnpcbohhpnfglgohlbhfongabi?utm_source=item-share-cb


## Project Structure

```
software_testing/
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── templates/         
│   └── index.html     # Main frontend template
└── tests/
    ├── test_app.py            # Unit tests
    └── test_functional_blaze.py # Functional tests
```

## Dependencies

- Flask: Web framework
- Selenium: Browser automation for testing
- undetected-chromedriver: ChromeDriver management
- pytest: Testing framework
- Pillow: Image processing
- requests: HTTP client

## Notes

- The functional tests use Selenium with Chrome in automated mode
- Tests use element IDs and classes for reliable element selection
- The application must be running before executing functional tests
