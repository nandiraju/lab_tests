# Quick Start Guide for Lab Tests

## Installation

```bash
# Clone the repository
git clone https://github.com/nandiraju/lab_tests.git
cd lab_tests

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

### Quick Test Run
```bash
python run_tests.py
```

### Run Only Pytest Tests
```bash
pytest tests/ -v
```

### Run Only Custom Framework Tests
```bash
python tests/demo_custom_framework.py
```

### Run Tests with Coverage
```bash
pytest tests/ --cov=lab_tests --cov-report=html
```

## Creating Your Own Tests

### Using Pytest

Create a new file in `tests/` directory starting with `test_`:

```python
# tests/test_mymodule.py
def test_my_function():
    result = my_function(2, 3)
    assert result == 5
```

### Using Custom Lab Framework

```python
from lab_tests import LabTest, LabTestRunner

class MyCustomTest(LabTest):
    def run(self):
        self.assert_equal(1 + 1, 2, "Addition works")
        self.assert_true(True, "True is true")

# Run the test
runner = LabTestRunner()
runner.add_test(MyCustomTest("My Test", "Test description"))
runner.run_all()
```

## Available Assertions (Custom Framework)

- `assert_equal(actual, expected, message)` - Check if two values are equal
- `assert_true(condition, message)` - Check if condition is True
- `assert_false(condition, message)` - Check if condition is False

## Project Files

- `lab_tests/` - Main package with framework and modules
- `tests/` - All test files
- `run_tests.py` - Main test runner
- `pytest.ini` - Pytest configuration
- `setup.py` - Package installation setup
- `requirements.txt` - Python dependencies

## Tips

- Test files should start with `test_` for pytest to discover them
- Use descriptive test names that explain what is being tested
- Keep tests simple and focused on one thing
- Run tests frequently during development
