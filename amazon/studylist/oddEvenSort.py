def oddEven(arr):
  arr.sort()
  l = 0
  r = len(arr) - 1

  while l <= r:
    #even index = positive odd index = negative
    if l % 2 == 0 and arr[l] < 0:
      while r % 2 != 1:
        r -= 1
      tmp = arr[l]
      arr[l] = arr[r]
      arr[r] = tmp
    r -= 1
    l += 1
  return arr
       

print(oddEven(arr = [1, -1, 2, -2, 3, -3]))
print(oddEven(arr = [4, -3, -7, 6, 8, -1, -9, 2]))