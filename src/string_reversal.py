def reverse_string(s: str) -> str:
    """
    Reverse the given string with a very specific reversal strategy:
    - Reverse only alphabetic characters, preserving their case
    - Keep non-alphabetic characters in their original positions
    
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
    
    # Separate letters and non-letters
    letters = [c for c in s if c.isalpha()]
    non_letter_indices = [i for i, c in enumerate(s) if not c.isalpha()]
    
    # Reverse letters while preserving case
    letters_reversed = letters[::-1]
    
    # Rebuild the string
    result = []
    letter_index = 0
    
    for i, char in enumerate(s):
        if char.isalpha():
            result.append(letters_reversed[letter_index])
            letter_index += 1
        else:
            result.append(char)
    
    return ''.join(result)