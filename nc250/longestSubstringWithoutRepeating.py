class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #build hasmap to track occurrences
        seen = {}
        start = 0
        longest = 0

        for i, v in enumerate(s):
            if v in seen and seen[v] >= start:
                start = seen[v] + 1
            longest = max(longest, i - start + 1)
            seen[v] = i
        return longest