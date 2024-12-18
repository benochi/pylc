class Solution:
    def rob(self, nums: List[int]) -> int:
        current, highest = 0,0

        for n in nums:
            temp = max(n + current, highest)
            current = highest
            highest = temp
        return highest