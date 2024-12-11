class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        value = 0
        sign = 1
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        while i < len(s) and s[i].isdigit():
            value = value * 10 + int(s[i])
            i+=1
        
        value *= sign

        if value < -(2**31):
            return -(2**31)
        if value > 2 ** 31 -1:
            return 2 ** 31 - 1
        return value
