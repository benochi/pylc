# Problem: Distribute Apples in a 3x3 Grid
# You are given a 0-indexed 2D integer matrix grid of size 3 * 3, representing the number of apples in each cell. 
# The grid contains exactly 9 apples, and there can be multiple apples in a single cell.

# In one move, you can move a single apple from its current cell to any other cell if the two cells share a side.

# Return the minimum number of moves required to place one apple in each cell.

# Example 1:
# Input:
# grid = [[1, 1, 0], [1, 1, 1], [1, 2, 1]]
# Output:
# 3
# Explanation:
# One possible sequence of moves to place one apple in each cell is:

# Move one apple from cell (2,1) to cell (2,2).
# Move one apple from cell (2,2) to cell (1,2).
# Move one apple from cell (1,2) to cell (0,2).
# In total, it takes 3 moves to place one apple in each cell of the grid.
# It can be shown that 3 is the minimum number of moves required.

# Example 2:
# Input:
# grid = [[1, 3, 0], [1, 0, 0], [1, 0, 3]]
# Output:
# 4
# Explanation:
# One possible sequence of moves to place one apple in each cell is:

# Move one apple from cell (0,1) to cell (0,2).
# Move one apple from cell (0,1) to cell (1,1).
# Move one apple from cell (2,2) to cell (1,2).
# Move one apple from cell (2,2) to cell (2,1).
# In total, it takes 4 moves to place one apple in each cell of the grid.

# Constraints:
# grid.length == grid[i].length == 3
# 0 ≤ grid[i][j] ≤ 9
# The sum of grid is equal to 9.
from collections import deque

def apples(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    q = deque()
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    moves = 0

    # Add cells with more than 1 apple to the queue
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] > 1:
                q.append((r, c))

    # Distribute apples using BFS
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            row, col = r + dr, c + dc
            if ():
                # Move an apple
                matrix[r][c] -= 1
                matrix[row][col] += 1
                moves += 1
                q.append((row, col))  
                break

    return moves

print(apples([[1, 1, 0], [1, 1, 1], [1, 2, 1]])) # 3
print(apples([[1, 3, 0], [1, 0, 0], [1, 0, 3]])) # 4 
