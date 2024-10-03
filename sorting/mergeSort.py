# break down to single element array copies, compare to arrays and insert in order.
# recursion - 2 branches
# is mergesort stable? We can make it stable.
def mergeSort(arr, s, e):
    # starting index and ending index
    if e - s + 1 <= 1:
        return arr

    # middle index will typically round down.
    m = (s + e) / 2
    # sort first half
    mergeSort(arr, s, m)
    # sort second half
    mergeSort(arr, m + 1, e)

    merge(arr, s, m, e)
    return arr
