# Maximum Subarray Sum – Kadane’s Algorithm
# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

# Examples:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.


# Input: arr[] = {-2, -4}
# Output: –2
# Explanation: The subarray {-2} has the largest sum -2.


# Input: arr[] = {5, 4, 1, 7, 8}
# Output: 25
# Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# -109 ≤ arr[i] ≤ 104



def kadane(list):
  maxSum = list[0]
  curr = list[0]

  for i in range(1, len(list)):
    curr = max(list[i], curr + list[i])
    maxSum = max(maxSum, curr)

  return maxSum


print(kadane([2, 3, -8, 7, -1, 2, 3])) #11
print(kadane([-2, -4])) # -2 
print(kadane([5, 4, 1, 7, 8])) # 25