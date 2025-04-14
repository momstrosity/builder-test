import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_same_numbers():
    """Test GCD when both numbers are the same"""
    assert gcd_using_prime_factors(10, 10) == 10

def test_gcd_coprime_numbers():
    """Test GCD for coprime numbers"""
    assert gcd_using_prime_factors(7, 11) == 1

def test_gcd_with_common_factors():
    """Test GCD for numbers with common prime factors"""
    assert gcd_using_prime_factors(24, 36) == 12

def test_gcd_one_is_multiple_of_other():
    """Test GCD when one number is a multiple of the other"""
    assert gcd_using_prime_factors(15, 45) == 15

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert gcd_using_prime_factors(1071, 462) == 21

def test_invalid_input_negative():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(-10, 20)

def test_invalid_input_zero():
    """Test that zero inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 20)

def test_invalid_input_type():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(10.5, 20)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors("10", 20)