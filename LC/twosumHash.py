class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in count:
                return [i, count[diff]]
            count[n] = i
        return []
