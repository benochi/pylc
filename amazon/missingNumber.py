#find missing number in sequence from 1-n
def find_missing_number(nums, n):
  #XOR all nums from 1 - n assuming positives. n+1 in case n is the missing num
  xor_full = 0
  for i in range(1, n + 1):
    xor_full ^= i
  # print(xor_full)
  #XOR of all numbers in the given array
  xor_arr = 0
  for num in nums:
    xor_arr ^= num
  # print(xor_arr)
  print(2 ^ 1)  
  # print(4 ^ 1)
  #missing num is  XOR of the two
  return xor_full ^ xor_arr

print(find_missing_number([1, 2, 4, 5], 5))  # Expected output: 3
# print(find_missing_number([1, 2, 3, 4], 5))

0111