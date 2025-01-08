# You are given an 
# 𝑚
# ×
# 𝑛
# m×n integer matrix grid, and two integers row and col. Each value in the grid represents the type of terrain at that location.

# Two cells are considered connected if they are adjacent (up, down, left, or right) and have the same terrain type.

# The perimeter of a connected component is defined as the number of edges that border cells that are not part of the connected component.

# Write a function to calculate the perimeter of the connected component that includes the cell at grid[row][col].

# Example:
# Input 1:
# python
# Copy code
# grid = [[1, 1, 0], 
#         [1, 0, 0], 
#         [1, 1, 1]]
# row = 1
# col = 0
# Output:
# 8

# Explanation:
# The connected component is [[1, 1, 0], [1, -, 0], [1, 1, 1]] (all 1s connected to grid[1][0]). Its perimeter is 8.

# Input 2:
# python
# Copy code
# grid = [[1, 1, 1], 
#         [1, 1, 1], 
#         [1, 1, 1]]
# row = 1
# col = 1
# Output:
# 0

# Explanation:
# The connected component is the entire grid. Its perimeter is 0 because there are no edges bordering cells outside the component.

# Input 3:
# python
# Copy code
# grid = [[1, 2, 2], 
#         [2, 3, 2], 
#         [1, 2, 3]]
# row = 0
# col = 1
# Output:
# 4

# Explanation:
# The connected component is [[1, 2, -], [-, 3, -], [-, -, -]]. Its perimeter is 4.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 ≤ m,n ≤50
# 1 ≤ grid[i][j] ≤ 1000
# 0 ≤ row < m
# 0 ≤ col < n


from collections import deque

def terrain(grid, row, col):
  ROWS, COLS = len(grid), len(grid[0])
  q = deque([(row, col)])
  value = grid[row][col]
  visit = set()
  edges = 0
  directions = [[0,1], [1,0], [0,-1],[-1,0]]

  while q:
    r, c = q.popleft()
    for dr, dc in directions:
      curr_r, curr_c = dr + r, dc + c
      if(0 <= curr_r < ROWS or
        0 <= curr_c < COLS or
        (curr_r, curr_c) in visit or
        grid[curr_r][curr_c] != value
        ): 
        edges += 1
        continue
      q.append((curr_r, curr_c))
      visit.add((curr_r, curr_c))
  return edges
      




print(terrain([[1, 2, 2], [2, 3, 2], [1, 2, 3]],0,1)) 
print(terrain([[1, 1, 1], [1, 1, 2], [1, 2, 3]],0,0)) # 4
print(terrain([[1, 1, 1], [1, 1, 2], [1, 2, 3]], 0, 0))
