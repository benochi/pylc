class Solution(object):
    def guessNumber(self, n):
        # """
        # :type n: int
        # :rtype: int
        # """
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            res = guess(mid)
            if res == 1:
                l = mid + 1
            elif res == -1:
                r = mid - 1
            else:
                return mid
