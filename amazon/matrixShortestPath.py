def bfs(grid):
  ROWS, COLS = len(grid), len(grid[0])

  visit = set()
  q = deque()
  q.append(0,0)
  visit.add(0,0)

  length = 0
  while q:
    for i in range(len(q)):
      r, c = q.popleft()
      if r == ROWS - 1 and c == COLS -1:
        return length
      
      directions =[[0,1], [0,-1], [1,0], [-1,0]]
      for dr, dc in directions:
        row, col = dr + r, dc + c
        if (min(row, col)< 0 or
          row == ROWS or col == COLS or
          (row, col) in visit or grid[row][col] ==1):
          continue
        q.append((row,col))
        visit.add((row,col))
    length += 1
print(bfs(grid))
