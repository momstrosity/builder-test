def search_sorted_matrix(matrix, target):
    """
    Search for a target value in a 2D matrix where inner lists are sorted in ascending order.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The target value to find
    
    Returns:
        bool: True if the target is found, False otherwise
    
    Time Complexity: O(m + log(n)), where m is the number of rows and n is the number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If the matrix is empty or inconsistent
    """
    # Input validation
    if not matrix or not matrix[0]:
        return False
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check matrix consistency
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("Matrix rows must have consistent length")
    
    # Find the potential row via binary search on row first elements
    rows = len(matrix)
    left, right = 0, rows - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If target is out of current row's range, adjust search
        if matrix[mid][0] > target:
            right = mid - 1
        elif matrix[mid][-1] < target:
            left = mid + 1
        else:
            # Target might be in this row, do binary search within the row
            return binary_search(matrix[mid], target)
    
    return False

def binary_search(row, target):
    """
    Perform binary search on a sorted row to find the target.
    
    Args:
        row (List[int]): A sorted list of integers
        target (int): The target value to find
    
    Returns:
        bool: True if target is found, False otherwise
    """
    left, right = 0, len(row) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if row[mid] == target:
            return True
        elif row[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False