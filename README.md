# Assignment 4: Professional Calculator Command-Line Application

A modular command-line calculator with REPL interface, demonstrating clean architecture, comprehensive error handling, and 100% test coverage.

## Features

- **REPL Interface**: Continuous user interaction with professional command parsing
- **Arithmetic Operations**: add, subtract, multiply, divide, power (bonus)
- **Error Handling**: Both LBYL and EAFP paradigms implemented
- **Factory Pattern**: Dynamic calculation creation with CalculationFactory
- **Input Validation**: Comprehensive format validation and error handling
- **History Management**: Session-based calculation history
- **Special Commands**: help, history, exit
- **100% Test Coverage**: 79 comprehensive tests

## Setup Instructions

### Installation
```bash
# Clone repository
git clone https://github.com/Pruthul15/assignment-4.git
cd assignment-4

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Run Calculator
```bash
python main.py
```

### Example Session
```
Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.

>> add 10 5
Result: AddCalculation: 10.0 + 5.0 = 15.0

>> power 2 3
Result: PowerCalculation: 2.0 Power 3.0 = 8.0

>> divide 10 0
Error: Division by zero is not allowed.
Please enter a non-zero divisor.

>> history
Calculation History:
1. AddCalculation: 10.0 + 5.0 = 15.0
2. PowerCalculation: 2.0 Power 3.0 = 8.0

>> exit
Thank you for using the Professional Calculator!
```

### Available Operations
- `add` - Addition
- `subtract` - Subtraction  
- `multiply` - Multiplication
- `divide` - Division (with zero protection)
- `power` - Exponentiation

### Special Commands
- `help` - Display usage instructions
- `history` - Show calculation history
- `exit` - Quit calculator

## Project Structure
```
assignment-4/
├── .github/workflows/python-app.yml  # CI/CD pipeline
├── app/
│   ├── calculator/__init__.py         # REPL interface
│   ├── calculation/__init__.py        # Calculation classes & factory
│   └── operation/__init__.py          # Mathematical operations
├── tests/
│   ├── conftest.py                    # Test configuration
│   ├── test_calculation.py            # Calculation tests
│   ├── test_calculator.py             # REPL tests
│   └── test_operations.py             # Operation tests
├── main.py                            # Entry point
├── requirements.txt                   # Dependencies
└── README.md
```

## Architecture & Design Patterns

### Factory Pattern
Dynamic calculation creation using decorator registration:
```python
@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    def compute(self) -> float:
        return Operation.add(self.a, self.b)
```

### Error Handling Paradigms
- **LBYL**: Input validation before processing
- **EAFP**: Try-except blocks for runtime errors

### Best Practices Applied
- **DRY Principle**: No code duplication
- **Modular Design**: Clean separation of concerns
- **Abstract Base Classes**: Consistent interfaces
- **Comprehensive Testing**: 100% coverage with edge cases

## Testing

### Run Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=app tests/

# Coverage report
pytest --cov=app --cov-report=html tests/
```

### Test Results
- **79 Total Tests**: Comprehensive unit and parameterized tests
- **100% Coverage**: All code paths tested
- **Edge Cases**: Division by zero, invalid inputs, error scenarios

## CI/CD Pipeline

GitHub Actions automatically:
- Runs all tests on every push
- Enforces 100% test coverage
- Fails build if coverage drops below 100%
- Validates code quality

## Requirements Met

- ✅ **REPL Interface**: Professional command-line interaction
- ✅ **Arithmetic Operations**: All required operations plus bonus power
- ✅ **Error Handling**: LBYL and EAFP paradigms demonstrated
- ✅ **Factory Pattern**: CalculationFactory implementation
- ✅ **Input Validation**: Comprehensive error handling
- ✅ **History Management**: Session calculation tracking
- ✅ **Testing**: 100% coverage with 79 tests
- ✅ **Documentation**: Code comments and docstrings
- ✅ **CI/CD**: GitHub Actions integration
- ✅ **Best Practices**: DRY principle and modular design

## Dependencies
```txt
pytest>=8.3.3
pytest-cov>=6.0.0
coverage>=7.6.1
```

---
