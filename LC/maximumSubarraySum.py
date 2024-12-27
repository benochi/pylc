class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        currSum = 0
        l = 0
        window = set()

        for r in range(len(nums)):
            while nums[r] in window:
                window.remove(nums[l])
                currSum -= nums[l]
                l += 1

            window.add(nums[r])
            currSum += nums[r]

            if r - l + 1 == k:
                maxSum = max(maxSum, currSum)
                window.remove(nums[l])
                currSum -= nums[l]
                l += 1
            
        return maxSum