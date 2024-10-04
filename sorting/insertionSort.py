# Insertion Sort Algorithm
# 1. Iterate through the array starting from the second element.
# 2. For each element, compare it to its predecessors and insert it into the correct position
#    among the previously sorted elements on its left.
# 3. Shift elements as needed to make room for the element being inserted.
# 4. This is an iterative algorithm, not recursive, which makes it efficient for small or nearly sorted datasets.
# 5. Time Complexity: O(n^2) in the worst case. Suitable for small or partially sorted arrays.
def insertionSort(arr):
    for i in range(len(arr) - 1):
        while i >= 0 and arr[i + 1] < arr[i]:
            tmp = arr[i + 1]
            arr[i + 1] = arr[i]
            arr[i] = tmp
            i -= 1
            print(i)
    return arr


print(insertionSort([1, 4, 5, 6, 2, 3, 8]))
# print(insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
