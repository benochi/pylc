# Smallest window that contains all characters of string itself

# Given a string, find the smallest window length with all distinct characters of the given string. For eg. str = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca” .

# Input: aabcbcdbca
# Output: dbca
# Explanation: 
# Possible substrings= {aabcbcd, abcbcd, 
# bcdbca, dbca....}
# Of the set of possible substrings 'dbca' 
# is the shortest substring having all the 
# distinct characters of given string. 

# Input: aaab
# Output: ab
# Explanation: 
# Possible substrings={aaab, aab, ab}
# Of the set of possible substrings 'ab' 
# is the shortest substring having all 
# the distinct characters of given string.
from collections import Counter

def wacky(str):
  count = Counter(str)
  distinct = {}
  l = 0
  smallestWindow = float('inf')
  minWindow = ""

  for r, c in enumerate(str):
        distinct[c] = distinct.get(c, 0) + 1

        while len(distinct) == len(count):
            if r - l + 1 < smallestWindow:
                smallestWindow = r - l + 1
                minWindow = str[l:r+1]

            distinct[str[l]] -= 1
            if distinct[str[l]] == 0:
                del distinct[str[l]]
            l += 1

  return minWindow

print(wacky("aabcbcdbca")) #dbca
print(wacky("aaab")) #ab