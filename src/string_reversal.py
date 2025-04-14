def reverse_string(s: str) -> str:
    """
    Reverse the given string with a specific reversal strategy:
    - Reverse only alphabetic characters
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
    
    # Separate alphabetic and non-alphabetic characters
    result = list(s)
    letters = [c for c in s if c.isalpha()]
    letters_reversed = letters[::-1]
    
    # Replace alphabetic characters with reversed letters
    letter_index = 0
    for i in range(len(result)):
        if result[i].isalpha():
            result[i] = letters_reversed[letter_index]
            letter_index += 1
    
    return ''.join(result)