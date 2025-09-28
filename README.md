# Assignment 4: Professional Calculator Command-Line Application

**Author: Pruthul Patel**  
**Date: September 28, 2025**  
**Course: IS 601 - Programming with Python**

A modular command-line calculator with REPL interface, demonstrating clean architecture, comprehensive error handling, and 100% test coverage with modulus functionality.

## 🎯 Assignment Requirements Completed

✅ **Repository Setup**: Git repository with proper directory structure  
✅ **REPL Interface**: Continuous user interaction with professional command parsing  
✅ **Arithmetic Operations**: add, subtract, multiply, divide, power, modulus  
✅ **User Prompts**: Clear instructions and feedback  
✅ **Input Validation**: Comprehensive format validation and error handling  
✅ **Error Handling**: Both LBYL and EAFP paradigms implemented  
✅ **Calculation Management**: Factory pattern with history tracking  
✅ **Special Commands**: help, history, exit  
✅ **DRY Principle**: No code duplication, modular design  
✅ **100% Test Coverage**: 98 comprehensive tests with pytest  
✅ **Documentation**: Detailed comments, docstrings, and README  
✅ **GitHub Actions**: Automated testing with coverage enforcement  

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/Pruthul15/assignment4.git
cd assignment4

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run Calculator
```bash
python main.py
```

### Example Usage
```bash
# Basic operations
add 10 5
subtract 20 8
multiply 4 7
divide 15 3

# Advanced operations
power 2 3
modulus 10 3

# Error handling examples
divide 10 0
modulus 15 0

# Special commands
help
history
exit
```

## 📁 Project Structure

```
assignment4/
├── .github/workflows/
│   └── python-app.yml           # GitHub Actions CI/CD
├── app/
│   ├── __init__.py              # Package initialization
│   ├── calculation/
│   │   └── __init__.py          # Calculation classes & factory
│   ├── calculator/
│   │   └── __init__.py          # REPL interface
│   └── operation/
│       └── __init__.py          # Mathematical operations
├── tests/
│   ├── conftest.py             # Test configuration
│   ├── test_calculation.py     # Calculation tests (44 tests)
│   ├── test_calculator.py      # REPL tests (20 tests)
│   └── test_operations.py      # Operation tests (34 tests)
├── main.py                      # Application entry point
├── pytest.ini                  # Pytest configuration
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## 🔧 Key Features

### REPL Interface
Professional command-line interface with continuous user interaction:
```
Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.

>> add 10 5
Result: AddCalculation: 10.0 Add 5.0 = 15.0

>> help
Available operations: add, subtract, multiply, divide, power, modulus
Special commands: help, history, exit
```

### Arithmetic Operations
- **Basic**: add, subtract, multiply, divide
- **Advanced**: power, modulus
- **All operations**: Support decimal numbers and proper error handling

### Error Handling Implementation

#### LBYL (Look Before You Leap)
```python
# Check conditions before processing
if not user_input:
    continue
if command == "help":
    display_help()
```

#### EAFP (Easier to Ask Forgiveness than Permission)
```python
# Try operation and handle exceptions
try:
    operation, num1_str, num2_str = user_input.split()
    num1, num2 = float(num1_str), float(num2_str)
except ValueError:
    print("Invalid input. Please follow format: <operation> <num1> <num2>")
```

### Factory Pattern Implementation
Dynamic calculation creation with decorator registration:
```python
@CalculationFactory.register_calculation('modulus')
class ModulusCalculation(Calculation):
    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot perform modulus by zero.")
        return Operation.modulus(self.a, self.b)
```

### Calculation History
Session-based tracking of all calculations with display functionality:
```bash
>> history
Calculation History:
1. AddCalculation: 10.0 Add 5.0 = 15.0
2. PowerCalculation: 2.0 Power 3.0 = 8.0
3. ModulusCalculation: 10.0 Modulus 3.0 = 1.0
```

## 🧪 Testing

### Run Tests
```bash
# All tests with coverage
pytest --cov=app tests/

# Generate HTML coverage report
pytest --cov=app --cov-report=html tests/

# Verify 100% coverage requirement
coverage report --fail-under=100

# Verbose test output
pytest -v
```

### Test Results
- **98 Total Tests**: Complete unit and parameterized testing
- **100% Coverage**: All 149 statements and 22 branches covered
- **Edge Cases**: Division by zero, invalid inputs, error scenarios
- **Parameterized Tests**: Multiple scenarios tested efficiently

### Test Structure
- **test_calculation.py**: 44 tests covering all calculation classes
- **test_calculator.py**: 20 tests covering REPL interface  
- **test_operations.py**: 34 tests covering all mathematical operations

## 🤖 GitHub Actions Automation

Automated CI/CD pipeline that:
- Runs all tests on every push/pull request
- Enforces 100% test coverage requirement
- Fails build if coverage drops below 100%
- Tests on Ubuntu with Python 3.x

Configuration file: `.github/workflows/python-app.yml`

## 📚 Documentation

### Code Documentation
- **Function Documentation**: Every function includes comprehensive docstrings
- **Class Documentation**: All classes documented with purpose and usage
- **Inline Comments**: Complex logic explained with clear comments
- **Type Hints**: All functions include proper type annotations

### Error Handling Examples

#### Division/Modulus by Zero
```bash
>> divide 10 0
Cannot divide by zero.
Please enter a non-zero divisor.

>> modulus 10 0
Cannot divide by zero.
Please enter a non-zero divisor.
```

#### Invalid Input Format
```bash
>> add ten five
Invalid input. Please follow the format: <operation> <num1> <num2>
Type 'help' for more information.
```

#### Unsupported Operation
```bash
>> logarithm 2 3
Unsupported calculation type: 'logarithm'. Available types: add, subtract, multiply, divide, power, modulus
Type 'help' to see the list of supported operations.
```

## 💡 Best Practices Applied

### DRY Principle
- No code duplication across operations
- Shared functionality extracted to base classes
- Consistent error handling patterns

### Modular Design
- Clean separation of concerns
- Operations module handles mathematical logic
- Calculator module manages user interface
- Calculation module implements business logic

### Professional Code Quality
- Abstract Base Classes for consistent interfaces
- Factory pattern for dynamic object creation
- Comprehensive error handling with user-friendly messages
- 100% test coverage ensuring reliability

## 🔍 Code Coverage

Current coverage metrics:
```
Name                          Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------- 
app/__init__.py                   0      0      0      0   100%
app/calculation/__init__.py      61      0      8      0   100%
app/calculator/__init__.py       65      0     10      0   100%
app/operation/__init__.py        23      0      4      0   100%
-------------------------------------------------------------
TOTAL                           149      0     22      0   100%
```

## 🛠️ Dependencies

The project uses minimal, focused dependencies for testing and coverage:

```
pytest==8.3.3        # Testing framework with parameterized tests
pytest-cov==6.0.0    # Coverage measurement plugin for pytest  
coverage==7.6.1      # Code coverage analysis tool
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 🔍 Technologies Used

- **Python 3.12**: Core programming language
- **pytest**: Testing framework with parameterized tests
- **pytest-cov**: Code coverage measurement
- **GitHub Actions**: Continuous integration and deployment
- **Virtual Environment**: Isolated dependency management

## 📋 Assignment Compliance

This project fully meets all Assignment 4 requirements:

### Core Requirements
- ✅ Repository setup with proper structure
- ✅ REPL interface implementation
- ✅ All arithmetic operations (add, subtract, multiply, divide, power, modulus)
- ✅ User prompts with clear instructions
- ✅ Input validation and error handling
- ✅ LBYL and EAFP paradigms demonstrated
- ✅ Calculation management with Factory pattern
- ✅ Special commands (help, history, exit)

### Quality Requirements  
- ✅ DRY principle application
- ✅ Modular design with clean architecture
- ✅ 100% test coverage with 98 comprehensive tests
- ✅ Detailed documentation and comments
- ✅ GitHub Actions automation with coverage enforcement

---

**Assignment 4 Complete** - Professional Calculator with 100% Test Coverage  
**Student**: Pruthul Patel | **Course**: IS 601 | **GitHub**: https://github.com/Pruthul15/assignment4