def reverse_string(s: str) -> str:
    """
    Reverse the given string manually, preserving all characters 
    and maintaining original number positions.
    
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
    
    # Track positions of non-digit characters
    non_digit_positions = [i for i, char in enumerate(chars) if not char.isdigit()]
    
    # Sort non-digit characters in reverse order
    non_digit_chars = [chars[i] for i in non_digit_positions]
    non_digit_chars = non_digit_chars[::-1]
    
    # Rebuild the string with original number positions
    result = []
    non_digit_index = 0
    for i in range(len(chars)):
        if i in non_digit_positions:
            result.append(non_digit_chars[non_digit_index])
            non_digit_index += 1
        else:
            result.append(chars[i])
    
    return ''.join(result)