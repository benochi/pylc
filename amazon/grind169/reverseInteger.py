class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1])
        value = sign * reversed_num
        


        if value <= -(2**31) or value >= (2**31):
            return 0
        return value