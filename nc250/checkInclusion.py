class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if s1Count == window:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            window[ord(s2[i]) - ord('a')] +=1

            if s1Count == window:
                return True
        return False