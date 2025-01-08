testArrs = [[3, 1, 4, 1, 5, 9],
[7, 7, 7, 7, 7],
[1, 2, 3, 4, 5, 6],
[10, 9, 8, 7, 6, 5],
[-3, 1, -4, 1, 5, -9],
[0, 0, 1, 0, 2, 0, 3],
[5, 3, 8, 3, 1, 8]]


def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])

  merge(left, right, arr)

  return arr
  #two pointers for merging
def merge(arr1, arr2, mainArr):
  l = 0
  r = 0
  k = 0
  while l < len(arr1) and r < len(arr2):
    if arr1[l] < arr2[r]:
      mainArr[k] = arr1[l]
      l += 1
    else:
      mainArr[k] = arr2[r]
      r += 1
    k += 1
  
  while l < len(arr1):
    mainArr[k] = arr1[l]
    l += 1
    k += 1
  
  while r < len(arr2):
    mainArr[k] = arr2[r]
    r += 1
    k += 1


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



for a in testArrs:
  print(mergeSort(a))
  print("merge ^")
  print(quickSort(a))
  print("quick ^")