def rotate(text, key):
    """
    Encrypts the given text using a rotational cipher with the specified key.

    A rotational cipher, also known as a Caesar cipher, shifts each letter in the
    input text by a fixed number of positions down the alphabet. Non-alphabetic
    characters are not modified.

    Args:
        text (str): The input text to be encrypted.
        key (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted text after applying the rotational cipher.
    """
    cipher = ""
    for char in text:
        if char.isalpha():
            # Calculate the shift value for the current character
            shift = key % 26

            # Encrypt the current character based on its case, by shifting the character by the specified number of positions
            """
            ord() returns the Unicode code point of a character
            chr() returns the character that corresponds to the given Unicode code point
            The formula below calculates the new character position after shifting by the specified number of positions
            ord(char) - ord('a') gets the position of the character in the lowercase alphabet
            (ord(char) - ord('a') + shift) % 26 gets the new position after shifting by the specified number of positions
            (ord(char) - ord('a') + shift) % 26 + ord('a') gets the new character after shifting by the specified number of positions
            """
            if char.islower():
                cipher += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                cipher += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Non-alphabetic characters are not modified
            cipher += char
    return cipher
