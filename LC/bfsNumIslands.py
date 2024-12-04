import collections

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

class Solution:
  def numIslands(self, grid):
    # handle setup
    if not grid:
      return 0
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    #handle bfs, set up q, add r,c to visit, handle direction checks
    def bfs(r, c):
      q = collections.deque()
      visit.add((r,c))
      q.append((r,c))

      while q:
        row, col = q.popleft() #use pop for DFS
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
      
        for dr, dc in directions: 
          r, c = row + dr, col + dc #simplify variable (row,col) from q add to dr, dc
          #check for in bounds, and "1" and if neighbors are not visited or in q then we add them.
          if(r in range(rows) and
             c in range(cols) and
             grid[r][c] == "1" and
             (r,c) not in visit):
            q.append((r,c))
            visit.add((r,c))


    
    #set up grid traversal loops
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "1" and (r,c) not in visit:
          bfs(r,c)
          islands += 1
    
    return islands

solution = Solution()
print(solution.numIslands(grid))