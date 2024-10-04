class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort to red/white/blue
        if not nums:
            return []

        counts = [0] * (max(nums) + 1)

        for i in range(len(nums)):
            counts[nums[i]] += 1

        j = 0
        for i in range(len(counts)):
            while counts[i] > 0:
                nums[j] = i
                j += 1
                counts[i] -= 1

        return nums
