# Given a non-empty array of integers nums, where every element appears twice except for one,
# find the element that does not appear twice.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # TODO: Implement the logic described in the outline
        # Steps (no solution code yet):
        # 1. Initialize a variable to hold cumulative XOR.
        # 2. Loop through each element and XOR it with the variable.
        # 3. The result after processing all elements is the unique number.
        pass
        
        result = 0
        for num in nums:
            result ^= num
        return result

# Example 1:
# nums = [2, 2, 1]
# Expected output: 1

# Example 2:
# nums = [4, 1, 2, 1, 2]
# Expected output: 4

# Example 3:
# nums = [1]
# Expected output: 1

# Example 4:
# nums = [0, 1, 0, 1, 99]
# Expected output: 99

sol = Solution()
print(sol.singleNumber([2, 2, 1]))       # Expected 1
print(sol.singleNumber([4, 1, 2, 1, 2])) # Expected 4
print(sol.singleNumber([1]))             # Expected 1
print(sol.singleNumber([0, 1, 0, 1, 99]))# Expected 99