def reverse_string(s: str) -> str:
    """
    Reverse the given string with a very specific reversal strategy:
    - Reverse the order of special characters and letters
    - Maintain original positions of digits and spaces
    
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
    
    # Separate different character types
    spec_letter_chars = [c for c in s if not c.isdigit() and not c.isspace()]
    
    # Reverse special characters and letters
    spec_letter_chars_reversed = spec_letter_chars[::-1]
    
    # Rebuild the string
    result = []
    spec_letter_index = 0
    
    for char in s:
        if char.isdigit() or char.isspace():
            result.append(char)
        else:
            result.append(spec_letter_chars_reversed[spec_letter_index])
            spec_letter_index += 1
    
    return ''.join(result)