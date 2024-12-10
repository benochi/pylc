class RangeXOR:
  def __init__(self, nums):
    self.prefix_xor = [0]
    for num in nums:
      self.prefix_xor.append(self.prefix_xor[-1] ^ num)

  def query(self, l, r):
    #0 based index assumed
    return self.prefix_xor[r+1] ^ self.prefix_xor[1]
    
# Example:
# nums = [1, 2, 3, 4]
# prefix_xor = [0, 1, 3, 0, 4] because:
# 0 ^ 1 = 1
# 1 ^ 2 = 3
# 3 ^ 3 = 0
# 0 ^ 4 = 4
#
# XOR(1 to 2) (0-based, i.e. elements [2,3]) is prefix_xor[3] ^ prefix_xor[1] = 0 ^ 1 = 1
nums = [1, 2, 3, 4]
rx = RangeXOR(nums)
print(rx.query(1, 2))  # XOR of nums[1..2] = 2 ^ 3 = 1