from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.
    
    Args:
        url (str): The URL to parse.
    
    Returns:
        Dict[str, Any]: A dictionary containing URL components:
        - scheme: The URL scheme (protocol)
        - netloc: The network location (domain)
        - path: The URL path
        - params: URL parameters
        - query: A dictionary of query parameters
        - fragment: The URL fragment
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Check for empty or invalid URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        
        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Convert query parameters to their single value if only one exists
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': query_params,
            'fragment': parsed_url.fragment
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")