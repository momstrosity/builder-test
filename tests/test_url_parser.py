import pytest
from src.url_parser import parse_url

def test_parse_full_url():
    """Test parsing a complete URL with all components."""
    url = "https://www.example.com/path/to/page?name=John&age=30#section1"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/path/to/page',
        'params': '',
        'query': {'name': 'John', 'age': '30'},
        'fragment': 'section1'
    }

def test_parse_url_with_multiple_query_params():
    """Test URL with multiple values for the same query parameter."""
    url = "http://test.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'http',
        'netloc': 'test.com',
        'path': '/search',
        'params': '',
        'query': {'tag': ['python', 'programming']},
        'fragment': ''
    }

def test_parse_simple_url():
    """Test parsing a simple URL with minimal components."""
    url = "https://example.com"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'example.com',
        'path': '',
        'params': '',
        'query': {},
        'fragment': ''
    }

def test_parse_url_with_port():
    """Test URL with a port number."""
    url = "http://localhost:8000/api"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'http',
        'netloc': 'localhost:8000',
        'path': '/api',
        'params': '',
        'query': {},
        'fragment': ''
    }

def test_invalid_url_raises_error():
    """Test that invalid URLs raise a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_url_with_special_characters():
    """Test URL with special characters in path and query."""
    url = "https://example.com/path%20with%20spaces?q=hello%20world"
    result = parse_url(url)
    
    assert result == {
        'scheme': 'https',
        'netloc': 'example.com',
        'path': '/path%20with%20spaces',
        'params': '',
        'query': {'q': 'hello world'},
        'fragment': ''
    }

def test_url_without_scheme():
    """Test URL without a scheme."""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result == {
        'scheme': '',
        'netloc': '',
        'path': 'example.com/path',
        'params': '',
        'query': {},
        'fragment': ''
    }