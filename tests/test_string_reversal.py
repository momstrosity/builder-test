import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test empty string reversal."""
    assert reverse_string("") == ""

def test_reverse_string_special_chars():
    """Test string reversal with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_reverse_string_palindrome():
    """Test palindrome string."""
    assert reverse_string("racecar") == "racecar"

def test_reverse_string_invalid_input():
    """Test invalid input raises TypeError."""
    with pytest.raises(TypeError):
        reverse_string(123)
    
    with pytest.raises(TypeError):
        reverse_string(None)
    
    with pytest.raises(TypeError):
        reverse_string(["list"])