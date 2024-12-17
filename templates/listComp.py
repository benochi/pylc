# 1. Adjacency List Initialization
def listComprehension(list):
    listMap = {i: [] for i in range(list)}  # Used in Graph problems
    return listMap

print("Adjacency List:", listComprehension(5))  # Test case: 5 nodes


# 2. Initialize a 2D Grid
def initializeGrid(rows, cols, value=0):
    grid = [[value for c in range(cols)] for r in range(rows)]  # Used for Matrix problems
    return grid

print("Initialized Grid:", initializeGrid(3, 3, 0))  # 3x3 grid with 0s


# 3. Flatten a 2D List
def flatten2DList(matrix):
    return [num for row in matrix for num in row]  # Useful for Matrix flattening

print("Flattened List:", flatten2DList([[1, 2], [3, 4]]))  # [[1, 2], [3, 4]] → [1, 2, 3, 4]


# 4. Filter List (Condition-Based Filtering)
def filterList(nums):
    return [x for x in nums if x % 2 == 0]  # Filters even numbers

print("Filtered List (Even Numbers):", filterList([1, 2, 3, 4, 5]))  # Output: [2, 4]


# 5. Transform List
def transformList(nums):
    return [num * num for num in nums]  # Squares each element

print("Transformed List (Squared):", transformList([1, 2, 3, 4]))  # Output: [1, 4, 9, 16]


# 6. Pairwise Combinations (Cartesian Product)
def pairListCombinations(list1, list2):
    return [(x, y) for x in list1 for y in list2]  # Useful for generating pairs

print("Pair all possible list Combinations:", pairListCombinations([1, 2], [3, 4]))
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]


# 7. Index-Based Mapping
def indexBasedMap(nums):
    return [(i, num) for i, num in enumerate(nums)]  # Used for problems where indices matter

print("Index-Value-Based Mapping:", indexBasedMap([10, 20, 30]))  # Output: [(0, 10), (1, 20), (2, 30)]


# 8.reshape Matrix
def reshapeMatrix(matrix):
    # Flip rows into columns, changing the shape of the matrix
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Reshaped Matrix (2x3 to 3x2):", reshapeMatrix([[1, 2, 3], [4, 5, 6]]))
# Output: [[1, 4], [2, 5], [3, 6]]

