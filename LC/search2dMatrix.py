def searchMatrix(matrix, target):
    for row in matrix:
        if row and row[0] <= target <= row[-1]:
            return searchRow(row, target)
    return False


def searchRow(row, target):
    l = 0
    r = len(row) - 1

    while l <= r:
        m = (l + r) // 2
        if row[m] < target:
            l = m + 1
        elif row[m] > target:
            r = m - 1
        else:
            return True
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 20))
print(searchMatrix([[1, 5, 9, 14]], 5))
print(searchMatrix([[1, 5, 9, 14]], 10))
print(searchMatrix([[5]], 5))
print(searchMatrix([[5]], 2))
print(searchMatrix([[1, 3, 5], [10, 11, 16]], 1))
print(searchMatrix([[1, 3, 5], [10, 11, 16]], 16))
print(searchMatrix([[], [], []], 3))
