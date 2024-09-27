def is_valid(isbn):
    """
    Check if the provided ISBN-10 number is valid.
    An ISBN-10 number is valid if:
    1. It consists of 10 characters, excluding hyphens.
    2. The first 9 characters are digits.
    3. The last character can be a digit or 'X' (which represents the value 10).
    4. The weighted sum of the digits (from 10 to 1) modulo 11 is 0.
    Args:
        isbn (str): The ISBN-10 number as a string, which may include hyphens.
    Returns:
        bool: True if the ISBN-10 number is valid, False otherwise.
    Example:
        >>> is_valid("3-598-21508-8")
        True
        >>> is_valid("3-598-21508-9")
        False
    """
    # Function implementation here
    numbers = []
    isbn = isbn.replace('-', '')
    
    for char in isbn:
        if char.isdigit():
            numbers.append(int(char))
        elif char == 'X' and char == isbn[-1]:
            numbers.append(10)
        else:
            return False
            
    if len(numbers) != 10:
        return False

    return sum(number * (10 - idx) for idx, number in enumerate(numbers)) % 11 == 0
