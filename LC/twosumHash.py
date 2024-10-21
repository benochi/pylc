class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n  # checking if difference is already in hashmap
            if diff in prevMap:
                return [prevMap[diff], i]  # return solution if it is.
            prevMap[n] = i
        return
