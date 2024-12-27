#brute force:class Solution:
    # def findPeakElement(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         if (i == 0 or nums[i] > nums[i - 1]) and (i == len(nums) - 1 or nums[i] > nums[i + 1]):
    #             return i

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid  # Move left
            else:
                l = mid + 1  # Move right
        return l