# Professional Calculator REPL – Assignment 4

A Python-based calculator application featuring an interactive REPL (Read-Eval-Print Loop), modular design, 100% test coverage, and CI/CD integration via GitHub Actions.

---

## 🚀 Features

- **Interactive REPL Interface** – user-friendly command-line calculator  
- **Supported Operations** – addition, subtraction, multiplication, division, power (exponentiation)  
- **Calculation History** – view all past calculations in session  
- **Error Handling** – input validation, division by zero checks, clear error messages  
- **Special Commands** – `help`, `history`, `exit`  
- **100% Test Coverage** – enforced via CI/CD pipeline  
- **Clean Architecture** – factory pattern, abstract base classes, modular code  

---

## 📁 Project Structure

assignment4/
├── .github/
│ └── workflows/ # GitHub Actions CI config
├── app/
│ ├── calculation/ # Calculation classes and factory
│ │ ├── init.py
│ │ └── pycache/
│ ├── calculator/ # REPL calculator interface
│ │ ├── init.py
│ │ └── pycache/
│ └── operation/ # Mathematical operations
│ ├── init.py
│ └── pycache/
├── htmlcov/ # Coverage HTML report (auto-generated)
├── tests/ # pytest test suite
│ ├── init.py
│ ├── conftest.py
│ ├── test_calculation.py
│ ├── test_calculator.py
│ ├── test_operations.py
│ └── pycache/
├── venv/ # Virtual environment (not tracked in Git usually)
├── .coverage # Coverage data file
├── .coveragerc # Coverage configuration
├── .gitignore # Git ignore rules
├── LICENSE # License file
├── README.md # Project documentation
├── pytest.ini # pytest configuration
├── requirements.txt # Dependencies
├── unit_content_draft.md # Draft notes
└── main.py # Application entry point



---

## 🛠 Installation & Setup

### Prerequisites
- Python 3.8+  
- pip  
- Git  

### Steps
```bash
# clone repo
git clone https://github.com/Pruthul15/assignment-4.git
cd assignment4

# create venv
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# install deps
pip install -r requirements.txt


Welcome to the Professional Calculator REPL!
Type 'help' for instructions or 'exit' to quit.

>> add 3 4
Result: AddCalculation: 3.0 Add 4.0 = 7.0

>> power 4 2
Result: PowerCalculation: 4.0 Power 2.0 = 16.0

>> power 4 -2
Result: PowerCalculation: 4.0 Power -2.0 = 0.0625

>> power -4 2
Result: PowerCalculation: -4.0 Power 2.0 = 16.0

>> power -4 -3
Result: PowerCalculation: -4.0 Power -3.0 = -0.015625

>> history
Calculation History:
1. AddCalculation: 3.0 Add 4.0 = 7.0
2. PowerCalculation: 4.0 Power 2.0 = 16.0
3. PowerCalculation: 4.0 Power -2.0 = 0.0625
4. PowerCalculation: -4.0 Power 2.0 = 16.0
5. PowerCalculation: -4.0 Power -3.0 = -0.015625

>> help
Available Commands:
- add <a> <b>: Addition
- subtract <a> <b>: Subtraction
- multiply <a> <b>: Multiplication
- divide <a> <b>: Division
- history: Show calculation history
- help: Show this help message
- exit: Exit the calculator

>> exit
Exiting calculator. Goodbye!


Testing:
pytest

Run with coverage:
pytest --cov=app tests/
coverage report --fail-under=100
coverage html
