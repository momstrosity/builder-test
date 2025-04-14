def reverse_string(s: str) -> str:
    """
    Reverse the given string with a very specific reversal strategy:
    - Reverse the order of special characters and letters
    - Preserve original positions of digits
    
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
    
    # Separate digits and non-digits
    non_digit_chars = [c for c in s if not c.isdigit()]
    non_digit_chars_reversed = non_digit_chars[::-1]
    
    # Rebuild the string
    result = []
    non_digit_index = 0
    
    for char in s:
        if char.isdigit():
            result.append(char)
        else:
            result.append(non_digit_chars_reversed[non_digit_index])
            non_digit_index += 1
    
    return ''.join(result)