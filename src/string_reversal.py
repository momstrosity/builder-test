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
    
    # Convert string to list for manipulation
    chars = list(s)
    
    # Reverse individual letters and symbols, preserving number positions
    letter_symbols = [char for char in chars if not char.isdigit()]
    letter_symbols_reversed = letter_symbols[::-1]
    
    # Rebuild the string
    result = []
    letter_symbol_index = 0
    for char in chars:
        if char.isdigit():
            result.append(char)
        else:
            result.append(letter_symbols_reversed[letter_symbol_index])
            letter_symbol_index += 1
    
    return ''.join(result)