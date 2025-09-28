
"""
Author: Pruthul Patel
Date: September 28, 2025
Assignment 4: Professional Calculator Command-Line Application
IS 601 - Programming with Python
"""


# conftest.py

import pytest
from app.calculation import CalculationFactory, PowerCalculation, ModulusCalculation

@pytest.fixture(autouse=True)
def ensure_calculations_registered():
    """Automatically ensure all calculations are registered before each test."""
    # This fixture runs automatically before each test
    # The import here ensures the PowerCalculation and ModulusCalculation decorators execute
    pass