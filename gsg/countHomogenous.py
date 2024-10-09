class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        totalCount = 0
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                totalCount += (count * (count + 1)) // 2
                totalCount %= mod
                count = 1

        totalCount += (count * (count + 1)) // 2
        totalCount %= mod

        return totalCount
