# Kth Smallest Element in a Matrix

# Given an integer array nums and an integer k, return the kth smallest element in the array.

# You cannot sort the array to solve the problem.

# Example 1:
# Input: 
# nums = [3, 2, 1, 5, 6, 4], k = 2
# Output:
# 2

# Example 2:
# Input:
# nums = [7, 10, 4, 3, 20, 15], k = 3
# Output:
# 7

# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
import heapq

def smallest(nums, k):
  if not nums:
    return []
  heapq.heapify(nums)
  i = 1
  while i < k:
    heapq.heappop(nums)
    i += 1

  return nums[0]

print(smallest(nums = [3, 2, 1, 5, 6, 4], k = 2))  # 3
print(smallest(nums = [7, 10, 4, 3, 20, 15], k = 3)) # 10 
# O(n + K log N)
# Space = 0(N)