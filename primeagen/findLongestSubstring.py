# find longest substring that doesn't repeat characters
# return length, characters are unique. 
# all characters are all ASCII including spaces. 
# str is empty return 0

def findLongestSubstring(s):
  #Sliding windows, not iterative. 
  chars = set()
  longest = 0
  start = 0

  for end in range(len(s)):
    while s[end] in chars:
      chars.remove(s[start])
      start += 1
    chars.add(s[end])
    longest = max(longest, end - start + 1)
      
  
  return longest

print(findLongestSubstring(s = "abcabcbb"))
print(findLongestSubstring(s = ""))
print(findLongestSubstring(s = "a"))
print(findLongestSubstring(s = "abcdef"))
print(findLongestSubstring(s = "aaaaaa"))
print(findLongestSubstring(s = "abc!@#abc"))
print(findLongestSubstring(s = "pwwkew"))
print(findLongestSubstring(s = "abcdabcde"))
print(findLongestSubstring(s = "123!abc!123!"))