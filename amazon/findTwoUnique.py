def find_two_unique(nums):
  #xor all elements
  xor_full = 0
  for num in nums:
    xor_full ^= num
  # The following line isolates the lowest set bit (rightmost '1' bit) in 'result'.
  # This bit must be different between the two unique numbers, 
  # which allows us to separate the array's elements into two groups.
  set_bit = xor_full & (-xor_full)  
  # We'll use x and y to hold the two unique numbers.
  x=0
  y=0
    # Check if the current element has the isolated set bit.
    # If yes, XOR it into 'x', otherwise into 'y'.
    # Elements that share that set bit go into 'x', 
    # others go into 'y'. This separates the two unique numbers.
  for num in nums:
    if num & set_bit:
      x ^= num
    else:
      y ^= num

  # At this point, x and y each hold one of the unique numbers.
  return x,y 

# Example:
# In [2, 3, 2, 5], 3 and 5 are unique, others (2 and 2) form pairs.
print(find_two_unique([2, 3, 2, 5]))  # Expected output: (3, 5) or (5, 3)