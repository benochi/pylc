class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        targetCount = {}
        for char in t:
            targetCount[char] = 1 + targetCount.get(char, 0)
        
        windowCount = {}
        have, need = 0, len(targetCount)
        left = 0
        minLength = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            windowCount[char] = 1 + windowCount.get(char, 0)

            if char in targetCount and windowCount[char] == targetCount[char]:
                have += 1
            
            while have == need:
                # Update the result if we found a smaller window
                if (right - left + 1) < minLength:
                    minLength = right - left + 1
                    result = s[left:right + 1]

                # Remove the leftmost character and move the left pointer
                leftChar = s[left]
                windowCount[leftChar] -= 1
                if leftChar in targetCount and windowCount[leftChar] < targetCount[leftChar]:
                    have -= 1
                left += 1
        
        return result