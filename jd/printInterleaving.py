# Print all interleavings of given two strings
# Last Updated : 16 Aug, 2024
# Given two strings str1 and str2, write a function that prints all interleavings of the given two strings. 
# You may assume that all characters in both strings are different 

# Example: 

# Input: str1 = “AB”,  str2 = “CD”
# Output:
#     ABCD
#     ACBD
#     ACDB
#     CABD
#     CADB
#     CDAB

# Input: str1 = “AB”,  str2 = “C”
# Output:
#     ABC
#     ACB
#     CAB


def strings(s1, s2, result=""):
    if not s1 and not s2:
        print(result)
        return
    if s1:
        strings(s1[1:], s2[:], result + s1[0])
    if s2:
        strings(s1, s2[1:], result + s2[0])


str1 = "AB"
str2 = "CD"
strings(str2, str1)
