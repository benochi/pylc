class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subSets = [1] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    subSets[i] = max(subSets[i], 1 + subSets[j])
                    

        return max(subSets)