"""
Test calculator module using pytest.
"""
import pytest
from lab_tests.calculator import add, subtract, multiply, divide, is_even, is_positive


class TestCalculator:
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition function."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction function."""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0
    
    def test_multiply(self):
        """Test multiplication function."""
        assert multiply(3, 4) == 12
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
    
    def test_divide(self):
        """Test division function."""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(1, 2) == 0.5
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_is_even(self):
        """Test even number checker."""
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(3) is False
        assert is_even(0) is True
    
    def test_is_positive(self):
        """Test positive number checker."""
        assert is_positive(5) is True
        assert is_positive(0) is False
        assert is_positive(-5) is False
