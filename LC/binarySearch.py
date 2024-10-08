def binarySearch(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m

        return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binarySearch(arr, target))
