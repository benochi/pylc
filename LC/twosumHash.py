class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = Counter(nums)
        print(count)
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement exists in the Counter
            if complement in count:
                # If complement is the same as num, ensure there are at least 2 occurrences
                if complement == num and count[complement] > 1:
                    return [i, nums.index(complement, i + 1)]
                elif complement != num:
                    return [i, nums.index(complement)]
        return []
