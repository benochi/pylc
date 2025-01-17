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

def heapSort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
      swapped = False
      for j in range(n - i - 1):
         if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped= True
      if not swapped:
         break
  return arr
            
def insertionSort(arr):
  #moves element backwards until it is bigger than i or is arr[0]
  for i in range(1, len(arr)):
      tmp = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > arr[i]:
         arr[j + 1] = arr[j]
         j -= 1
      arr[j + 1] = tmp
  return arr


for a in testArrs:
  print(mergeSort(a))
  print("merge ^")
  print(quickSort(a))
  print("quick ^")
  print(heapSort(a))
  print("heap ^")
  print(bubbleSort(a))
  print("Bubble ^")
  print(insertionSort(a))
  print("Insertion ^")