class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        #s count and p count. 
        countP, countS = {}, {}
        for i in range(len(p)):
            countP[p[i]] = 1 + countP.get(p[i],0)
            countS[s[i]] = 1 + countS.get(s[i],0)

        res = [0] if countS == countP else []

        l = 0
        for r in range(len(p), len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            countS[s[l]] -= 1
           
            if countS[s[l]] == 0:
                countS.pop(s[l])
            l += 1
            if countS == countP:
                res.append(l)
        
        return res