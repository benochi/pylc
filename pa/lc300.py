#find longest increasing substring in nums arr

def lengthOfLIS(nums):
  if not nums:
      return 0
  n = len(nums)
  dp = [1] * n

  for i in range(1, n):
      for j in range(i):
          if nums[i] > nums[j]:
              dp[i] = max(dp[i], dp[j] + 1)
  print(dp)
  return max(dp)




print(lengthOfLIS([1,2,3,4,5,6,4,1,10,2,9]))
print(lengthOfLIS([7,7,7,7,7]))
print(lengthOfLIS([]))