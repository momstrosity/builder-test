def reverse_string(s: str) -> str:
    """
    Reverse the given string with a very specific reversal strategy:
    - Reverse the entire string
    - Return the modified string
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return immediately
    if not s:
        return s
    
    # Convert string to list of characters and reverse
    chars = list(s)
    
    # Create result by reversing entire input
    result = []
    for i in range(len(chars) - 1, -1, -1):
        result.append(chars[i])
    
    return ''.join(result)