# break into sub problems and sort those.
# iterative over recursion on this one.  Not that great for large data sets.
def insertionSort(arr):
    for i in range(len(arr) - 1):
        while i >= 0 and arr[i + 1] < arr[i]:
            tmp = arr[i + 1]
            arr[i + 1] = arr[i]
            arr[i] = tmp
            i -= 1
    return arr


print(insertionSort([1, 4, 5, 6, 2, 3, 8]))
print(insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(insertionSort([]))
print(
    insertionSort(
        [
            "z",
            "y",
            "x",
            "w",
            "v",
            "u",
            "t",
            "s",
            "r",
            "q",
            "p",
            "o",
            "n",
            "m",
            "l",
            "k",
            "j",
            "i",
            "h",
            "g",
            "f",
            "e",
            "d",
            "c",
            "b",
            "a",
        ]
    )
)
