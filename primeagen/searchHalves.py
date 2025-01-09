# Do you have an ordered array
# BINARY SEARCH
# check an array for target inside array

def checkHalves(arr, target):
  if not arr:
    return False
  
  start = 0
  end = len(arr) - 1

  while start <= end:
    mid = (start + end) // 2

    if target == arr[mid]:
      return True
    elif target < arr[mid]:
      end = mid - 1
    else:
      start = mid + 1
  return False


print(checkHalves([1, 2, 3, 4, 5, 6], 3))  # True
print(checkHalves([1, 2, 3, 4, 5, 6], 6))  # True
print(checkHalves([1, 2, 3, 4, 5, 6], 0))  # False

