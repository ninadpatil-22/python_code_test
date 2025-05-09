import pytest
from Math_utils import MathUtils

@pytest.fixture
def math_utils():
    return MathUtils()

def test_add(math_utils):
    assert math_utils.add(2, 3) == 5
    assert math_utils.add(-2, 2) == 0
    assert math_utils.add(-4, -6) == -10

def test_subtract(math_utils):
    assert math_utils.subtract(10, 5) == 5
    assert math_utils.subtract(0, 5) == -5
    assert math_utils.subtract(-3, -6) == 3

def test_multiply(math_utils):
    assert math_utils.multiply(4, 5) == 20
    assert math_utils.multiply(-3, 3) == -9
    assert math_utils.multiply(0, 100) == 0

def test_divide(math_utils):
    assert math_utils.divide(10, 2) == 5.0
    assert math_utils.divide(0, 3) == 0.0
    assert math_utils.divide(3, 0) == -1.0  # division by zero edge case
