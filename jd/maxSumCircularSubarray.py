class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        maxSum = float('-inf')
        curMax = 0
        minSum = float('inf')
        curMin = 0

        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)

            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)

        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)