# Lab Tests

A simple and flexible testing framework for laboratory experiments and tests.

## Features

- Custom lab test framework with base classes and assertions
- Integration with pytest for advanced testing capabilities
- Sample calculator module with comprehensive tests
- Easy-to-use test runner

## Installation

1. Clone this repository:
```bash
git clone https://github.com/nandiraju/lab_tests.git
cd lab_tests
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running All Tests

Use the main test runner to execute all tests:

```bash
python run_tests.py
```

### Running Pytest Tests Only

```bash
pytest tests/ -v
```

### Running Custom Framework Tests

```bash
python tests/demo_custom_framework.py
```

## Project Structure

```
lab_tests/
├── lab_tests/          # Main package
│   ├── __init__.py     # Custom test framework (LabTest, LabTestRunner)
│   └── calculator.py   # Sample calculator module
├── tests/              # Test directory
│   ├── test_calculator.py           # Pytest tests
│   └── demo_custom_framework.py     # Custom framework demo
├── run_tests.py        # Main test runner
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Custom Test Framework

The custom `LabTest` framework provides a simple way to create and run tests:

```python
from lab_tests import LabTest, LabTestRunner

class MyTest(LabTest):
    def run(self):
        self.assert_equal(2 + 2, 4, "Math should work")
        self.assert_true(True, "This should pass")

runner = LabTestRunner()
runner.add_test(MyTest("My Test", "Description"))
passed, failed = runner.run_all()
```

## Available Assertions

- `assert_equal(actual, expected, message)` - Assert two values are equal
- `assert_true(condition, message)` - Assert condition is true
- `assert_false(condition, message)` - Assert condition is false

## Testing with Pytest

Standard pytest tests are supported in the `tests/` directory:

```python
def test_example():
    assert 1 + 1 == 2
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
