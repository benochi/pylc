
#O(n log n) - O(n^2)  usually faster than merge sort, sometimes can be slower but rare. 
def quickSort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[len(arr) // 2]
  left = []
  mid = []
  right = []

  for x in arr:
    if x < pivot:
      left.append(x)
    elif x == pivot:
      mid.append(x)
    else:
      right.append(x)

  return quickSort(left) + mid + quickSort(right)

print(quickSort([1,10,19,9,12,4,3,5,17,11,16,8,88,92,92,100,10,14,13,13,8,8,8,8,7]))