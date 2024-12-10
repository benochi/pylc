"""Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that "pwke" is a subsequence, not a substring.
The length of s will be between 0 and 10,000.

The string s consists of English letters, digits, symbols, and spaces."""


def longestSubstring(s): 
    if len(s) == 0:
        return 0

    chars = set()

    start = 0
    count = 0

    for cur in range(len(s)):
        while s[cur] in chars:
            chars.remove(s[start])
            start += 1

        chars.add(s[cur])

        count = max(count, cur - start + 1)

    return count


print(longestSubstring("abcabcbb"))
print(longestSubstring("bbbbb"))
print(longestSubstring("pwwkew"))
print(longestSubstring(""))
print(longestSubstring("abcdefg"))
