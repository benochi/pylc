class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        if any(value >= 2 for value in count.values()):
            return True
        else:
            return False
