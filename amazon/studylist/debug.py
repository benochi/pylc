def find_first_repeated_char(s):
    """
    Function to find the first repeated character in a string.
    Returns the character or None if there are no repeated characters.
    """
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

# Test the function
print(find_first_repeated_char("swiss"))  # Expected: 's'
print(find_first_repeated_char("amazon"))  # Expected: 'a'
print(find_first_repeated_char("unique"))  # Expected: 'u'