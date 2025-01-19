# Question: Find the longest increasing subsequence in an array of integers.
# Method Signature: List<Integer> longestIncreasingSubsequence(int[] nums)
# Expectations:
# Correctly identify the longest increasing subsequence
# Handle edge cases such as empty arrays or all decreasing elements


def longestSequence(nums):
  if not nums:
      return 0
  
  n = len(nums)
  dp = [1] * n

  for i in range(1, n):
      for j in range(i):
          if nums[i] > nums[j]:
              dp[i] = max(dp[i], dp[j] + 1)
  
  return max(dp)

def LCIS(nums):
    if not nums:
        return []
    
    current_length = 1
    max_length = 1
    end_index = 0
    
    # Track current sequence length and update max when we find longer one
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                end_index = i
        else:
            current_length = 1
    
    # Return the sequence using the end index and length
    start_index = end_index - max_length + 1
    return nums[start_index:end_index + 1]

print(longestSequence([1,2,3,4,5,0,1,2,3,6,8])) #7
print(longestSequence([-1,-2,-3,-4,-5,])) #1
print(longestSequence([])) #0
print(longestSequence([1, 10, 5, 4, 8])) #2

print(LCIS([1,2,3,4,5,0,1,2,3,6,8])) #6
print(LCIS([-1,-2,-3,-4,-5,])) #1
print(LCIS([])) #0
print(LCIS([1, 10, 5, 4, 8])) #2