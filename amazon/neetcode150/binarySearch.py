

def binarySearch(arr, target):
  arr.sort()

  #l r pointers
  l = 0
  r = len(arr) -1
  while l <= r:
    mid = (l + r) // 2
    if target == arr[mid]:
      return arr[mid]
    elif arr[mid] < target:
      l = mid + 1
    else:
      r = mid - 1
  return False





print(binarySearch([1,4,5,2,3,4,6,7,0,1,2,-7,12,15], 12))
print(binarySearch([1,4,5,2,3,4,6,7,0,1,2,-7,12,15], 200))