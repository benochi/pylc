# Count Possible Decodings of a given Digit Sequence
# Last Updated : 02 Dec, 2024
# Let 1 represent ‘A’, 2 represent ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.  
# When decoding multiple interpretations can arise due to overlapping possibilities for how digits can be grouped into valid letter 
# mappings. Each mapping corresponds to a letter based on its numeric value (e.g., “1” maps to ‘A’, “2” to ‘B’, …, “26” to ‘Z’).

# Consider the input string “123”. There are three valid ways to decode it:

# “ABC”: The grouping is (1, 2, 3) → ‘A’, ‘B’, ‘C’
# “AW”: The grouping is (1, 23) → ‘A’, ‘W’
# “LC”: The grouping is (12, 3) → ‘L’, ‘C’
# Note: Groupings that contain invalid codes (e.g., “0” by itself or numbers greater than “26”) are not allowed.
# For instance, the string “230” is invalid because “0” cannot stand alone, and “30” is greater than “26”, so it cannot represent any 
# letter. The task is to find the total number of valid ways to decode a given string.

# Examples: 

# Input: digits = “121”
# Output: 3
# Explanation: The possible decodings are “ABA”, “AU”, “LA”


# Input: digits = “1324”
# Output: 3
# Explanation: The possible decodings are “ABCD”, “LCD”, “AWD”

def decodeHelper(digits, index):
    n = len(digits)

    # Base case: If we reach the end of the string,
    # return 1 as it signifies a valid decoding.
    if index >= n:
        return 1

    ways = 0

    # Single-digit decoding: check if current digit is not '0'.
    if digits[index] != '0':
        ways = decodeHelper(digits, index + 1)

    # Two-digit decoding: check if next two digits are valid.
    if (index + 1 < n and 
        ((digits[index] == '1' and digits[index + 1] <= '9') or 
         (digits[index] == '2' and digits[index + 1] <= '6'))):
      
        ways += decodeHelper(digits, index + 2)

    return ways





