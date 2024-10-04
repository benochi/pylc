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


# Optimized solution with two pointers.
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr


# Test the function
arr = [1, 3, 5, 6, 4, 2, 5, 8, 9, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)


print(quickSort([1, 3, 5, 6, 4, 2, 5, 8, 9, 7]))
