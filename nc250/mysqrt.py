class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l = 0
        r = x
        while l <= r:
            mid = (r+l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
