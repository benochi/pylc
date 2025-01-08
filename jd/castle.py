# Given a matrix of size N x M where each cell contains either 0 or 1. A group of connected 1s forms a castle. 
# Two 1s are considered connected if they share an edge (not diagonally). There is exactly one castle in the matrix. 
# Find the number of walls needed to protect the castle, where each outer edge of a 1 cell requires one wall.
# Example:
# Input: grid = [
# [0,0,1,0],
# [0,1,1,0],
# [0,0,1,0]
# ]
# Output: 10
# Constraints:

# 1 <= N, M <= 100
# grid[i][j] is 0 or 1
# Exactly one castle (connected group of 1s) exists
# Castle cells are connected horizontally/vertically only

# The key differences from your example are:

# Theme changed from island to castle
# Different grid example
# Same core logic but reframed context
from collections import deque
def castle(grid):
  ROWS, COLS = len(grid), len(grid[0])
  walls = 0
  q = deque()
  visit = set()
  directions = [[0,1], [1,0],[-1,0],[0,-1]]

#O(N*M)
  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 1:
        q.append((r,c))
        visit.add((r,c))

  while q:
    r, c = q.popleft()
    for dr, dc in directions:
      row, col = dr + r, dc + c
      if (row < 0 or row >= ROWS or
          col < 0 or col >= COLS or
          grid[row][col] != 1
        ): 
        walls += 1
        continue
  
  return walls

print(castle([
[0,0,1,0],
[0,1,1,0],
[0,0,1,0]
])) #10

print(castle([
[0,1,1,0],
[0,1,1,0],
[0,0,0,0]
])) #8


