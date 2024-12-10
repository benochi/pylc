def find_two_unique(nums):
  #xor all elements
  xor_all = 0
  for num in nums:
    xor_all ^= num
  #find a set bit in xor_all(lowest set bit)
  set_bit = xor_all & (-xor_all)

  x = 0
  y = 0
  for num in nums:
    if num & set_bit:
      x ^= num
    else:
      y ^= num

  return x,y

# Example:
# In [2, 3, 2, 5], 3 and 5 are unique, others (2 and 2) form pairs.
print(find_two_unique([2, 3, 2, 5]))  # Expected output: (3, 5) or (5, 3)
  