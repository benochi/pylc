def smallest_string_with_unique_chars(s):
    """
    Find the smallest substring that contains all unique characters in the input string.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Smallest substring containing all unique characters
    """
    if not s:
        return ""
    
    # Get set of unique characters we need to find
    unique_chars = set(s)
    
    # If all characters are already unique, return the string
    if len(s) == len(unique_chars):
        return s
    
    # Initialize variables
    char_count = {}  # Keep track of character frequencies
    start = 0  # Window start
    min_length = float('inf')
    min_start = 0
    chars_found = 0  # Number of unique characters found in current window
    
    # Iterate through the string using sliding window
    for end in range(len(s)):
        # Add current character to window
        if s[end] not in char_count:
            char_count[s[end]] = 0
        char_count[s[end]] += 1
        
        # If this is first occurrence of character, increment chars_found
        if char_count[s[end]] == 1:
            chars_found += 1
        
        # Try to minimize window from start while maintaining all unique chars
        while chars_found == len(unique_chars):
            # Update minimum length if current window is smaller
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start
            
            # Remove character at start of window
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                chars_found -= 1
            start += 1
    
    # If no valid window found, return empty string
    if min_length == float('inf'):
        return ""
    
    return s[min_start:min_start + min_length]


    print(smallest_string_with_unique_chars("aabbaac"))         # Should return "baac"
    print(smallest_string_with_unique_chars("aaaa" ))          # Should return "a"
    print(smallest_string_with_unique_chars("abcde"))          # Should return "abcde"
    print(smallest_string_with_unique_chars(""))              # Should return ""
    print(smallest_string_with_unique_chars("aabbccaa"))      # Should return "abc"
