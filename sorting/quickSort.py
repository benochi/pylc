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
def quickSort(arr, low, high):
    if low < high:
        # Get the index where the pivot is placed after sorting
        pivotIndex = sortAroundPivot(arr, low, high)
        # Recursively apply quicksort to the left and right partitions
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)


def sortAroundPivot(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    smallerElementIndex = low - 1  # Keeps track of the "less than pivot" section

    for currentIndex in range(low, high):
        if arr[currentIndex] <= pivot:
            smallerElementIndex += 1
            # Swap the current element with the element at smallerElementIndex
            arr[smallerElementIndex], arr[currentIndex] = (
                arr[currentIndex],
                arr[smallerElementIndex],
            )

    # Move the pivot element to its correct position
    arr[smallerElementIndex + 1], arr[high] = arr[high], arr[smallerElementIndex + 1]
    return smallerElementIndex + 1


# Test the function
arr = [1, 3, 5, 6, 4, 2, 5, 8, 9, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)


print(quickSort([1, 3, 5, 6, 4, 2, 5, 8, 9, 7]))
