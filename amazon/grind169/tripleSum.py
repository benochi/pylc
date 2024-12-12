class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[i] + nums[r]
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                if cur_sum == target:
                    return target
                if cur_sum < target:
                    l += 1
                else:
                    r -= 1
            
        return closest_sum