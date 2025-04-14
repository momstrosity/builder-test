def reverse_string(s: str) -> str:
    """
    Reverse the given string manually, preserving all characters 
    and maintaining original character order.
    
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
    
    # Separate letters and other characters
    letters = [c for c in s if c.isalpha()]
    non_letters = [c for c in s if not c.isalpha()]
    
    # Reverse letters
    reversed_letters = letters[::-1]
    
    # Rebuild the string
    result = []
    letter_index = 0
    non_letter_index = 0
    
    for char in s:
        if char.isalpha():
            result.append(reversed_letters[letter_index])
            letter_index += 1
        else:
            result.append(char)
    
    return ''.join(result)