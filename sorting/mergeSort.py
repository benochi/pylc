# Merge Sort Algorithm
# 1. Recursively divide the array into two halves until single elements remain.
# 2. Use the merge function to combine two halves back together in sorted order.
# 3. The merge function compares elements from two sorted halves and merges them to form a single sorted array.


def merge(arr, start, mid, end):
    # Create temporary arrays for the two halves
    left = arr[start : int(mid) + 1]
    right = arr[int(mid) + 1 : end + 1]

    # Indices for traversing the two halves
    i, j, k = 0, 0, start

    # Merge the two halves back into the original array in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements of left half (if any)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements of right half (if any)
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, start, end):
    # Base case: single element (or empty) arrays are already sorted
    if end - start + 1 <= 1:
        return arr

    # Calculate the middle point of the current array
    mid = (start + end) // 2

    # Recursively sort the first half
    mergeSort(arr, start, mid)

    # Recursively sort the second half
    mergeSort(arr, mid + 1, end)

    # Merge the sorted halves together
    merge(arr, start, mid, end)

    return arr


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergeSort(arr, 0, len(arr) - 1)
print(sorted_arr)
