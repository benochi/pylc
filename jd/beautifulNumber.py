# Problem Statement:
# Beautiful Number

# A "beautiful number" is a positive integer whose prime factors are limited to 3, 7, and 11.

# Given an integer n, return the n-th beautiful number.

# Example 1:
# Input:
# n = 5
# Output:
# 21
# Explanation:
# The sequence of the first 5 beautiful numbers is:
# 1, 3, 7, 9, 11, 21...
# The 5th beautiful number is 21

# Example 2:
# Input:
# n = 1
# Output:
# 1
# Explanation:
# 1 has no prime factors, so it is included in the sequence

# Constraints:
# 1 <= n <= 1690
import heapq
def beautifulNum(n): 
  heap = [1]
  seen = {1}
  factors = [3, 7, 11]
    
  for _ in range(n):
    print(heap)
    beautiful = heapq.heappop(heap)
    for factor in factors:
        new_num = beautiful * factor
        if new_num not in seen:
          seen.add(new_num)
          heapq.heappush(heap, new_num)
    
  return beautiful

print(beautifulNum(5))