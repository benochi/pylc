# grab pivot value -> random value usually rightmost
# pivot = arr[-1]
# compare every other value to pivot and filter left or right based on comparison <= goes left, > goes right
# PsuedoCode:  base case, pivot, left right, recursion(left) + pivot + recursion(right)
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quickSort(left) + [pivot] + quickSort(right)


print(quickSort([1, 3, 5, 6, 4, 2, 5, 8, 9, 7]))
