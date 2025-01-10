# two sum, arr int nums and int target
# return 2 INDECES that add up to target
# each input will ahve 1 solution
# 3 order does NOT matter

#array of indeces, order doesn't matter -> 

def twoSum(nums, target):
  count = {}

  for i, v in enumerate(nums):
    diff = target - v
    if diff in count:
      return([count[diff], i])
    count[v] = i

print(twoSum(nums = [2, 7, 11, 15], target = 9))
print(twoSum(nums = [-3, 4, 3, 90], target = 0))
print(twoSum(nums = [3, 3],target = 6))
print(twoSum(nums = [1, 2, 3, 4, 5, 6], target = 10))
print(twoSum(nums = [10, 22, 1, 7], target = 17))

