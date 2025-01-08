def trySort(arr):
  #quickSort
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

  return trySort(left) + mid + trySort(right)








print(trySort([1,3,7,23,8,9,2]))