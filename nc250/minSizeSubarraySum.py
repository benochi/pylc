class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currentSum = 0
        minLength = float('inf')

        for r in range(len(nums)):
            currentSum += nums[r]

            while currentSum >= target:
                minLength = min(minLength, r - l + 1)
                currentSum -= nums[l]
                l += 1
        
        return minLength if minLength != float('inf') else 0
