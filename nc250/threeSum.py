class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for n in range(len(nums) -2):
            if n > 0 and nums[n] == nums[n - 1]:  
                continue

            mid = n + 1
            r = len(nums) - 1

            while mid < r:
                total = nums[n] + nums[mid] + nums[r]
                if total == 0:
                    res.append([nums[n], nums[mid], nums[r]])
                    while mid < r and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < r and nums[r] == nums[r - 1]:
                        r -= 1
                    mid += 1
                    r -= 1
                elif total < 0:
                    mid += 1
                else:
                    r -= 1
        return res