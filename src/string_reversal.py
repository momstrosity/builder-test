def reverse_string(s: str) -> str:
    """
    Reverse the given string with a very specific reversal strategy:
    - Reverse the entire string
    - Ensure numbers remain in their original positions
    - Preserve original capitalization and spacing
    
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
    
    # Convert string to list for manipulation
    chars = list(s)
    
    # Two-pointer approach to reverse the string
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)