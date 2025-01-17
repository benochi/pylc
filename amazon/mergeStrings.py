class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        total = len(word1) + len(word2) - 1
        res = ""

        while total >= 0:
            if p1 < len(word1):
                res += word1[p1]
                p1 += 1
            if p2 < len(word2):
                res += word2[p2]
                p2 += 1
            total -= 1
        return res