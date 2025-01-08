# def foo(n):
#   if n == 1:
#     return 1
  
#   #pre recursion n +
#   return n + foo(n-1)

# print(foo(100))

#can do pre, recursion, post recursion. 
arr=["#####E#",
    "#     #",
    "#S#####"]
directions = [[1,0],[0,1],[0,-1],[-1,0]]
def pathFind(maze, wall, start, end):
  seen = []
  path = []

  for p in path:
    s
  
def walk(maze, wall, curr, end, seen, path):
  if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
    return False
  if(maze[curr.x][curr.y] == wall):
    return False
  if curr.x == end.x and curr.y == end.y:
    path.push(end)
    return True
  if seen[curr.x][curr.y]:
    return False
  path.push(curr)
  for dr, dc in directions:
    [x,y] = directions[dr][dc]
    if walk(maze, wall, {x:curr.x+x, y:curr.y+y}, end, seen, path):
      return True
  path.pop()

  

  