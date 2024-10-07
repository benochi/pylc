class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2  # mid
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
