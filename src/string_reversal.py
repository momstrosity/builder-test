def reverse_string(s: str) -> str:
    """
    Reverse the given string with a very specific reversal strategy:
    - Reverse the order of letters in-place
    - Maintaining original positions of digits, spaces, and punctuation
    
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
    
    # Extract only alphabetic characters
    letters = [c for c in s if c.isalpha()]
    letters_reversed = letters[::-1]
    
    # Rebuild the string
    result = []
    letter_index = 0
    
    for char in s:
        if char.isalpha():
            result.append(letters_reversed[letter_index])
            letter_index += 1
        else:
            result.append(char)
    
    return ''.join(result)