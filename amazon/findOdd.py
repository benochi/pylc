#find the number that appears an odd number of times

def find_odd_occurring(nums):
  result = 0
  for num in nums:
    result ^= num
  return result


print(find_odd_occurring([2, 2, 1, 1, 1]))  # Expected output: 1