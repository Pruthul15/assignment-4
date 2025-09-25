# conftest.py

import pytest
from app.calculation import CalculationFactory, PowerCalculation, ModulusCalculation

@pytest.fixture(autouse=True)
def ensure_calculations_registered():
    """Automatically ensure all calculations are registered before each test."""
    # This fixture runs automatically before each test
    # The import here ensures the PowerCalculation and ModulusCalculation decorators execute
    pass