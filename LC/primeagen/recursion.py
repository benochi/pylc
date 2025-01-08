# def foo(n):
#   if n == 1:
#     return 1
  
#   #pre recursion n +
#   return n + foo(n-1)

# print(foo(100))

#can do pre, recursion, post recursion. 
directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

def pathFind(maze, wall, start, end):
    rows, cols = len(maze), len(maze[0])
    seen = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    def walk(curr, end):
        x, y = curr
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if maze[x][y] == wall:
            return False
        if seen[x][y]:
            return False
        if (x, y) == end:
            path.append((x, y))
            return True

        seen[x][y] = True
        path.append((x, y))

        for dr, dc in directions:
            if walk((x + dr, y + dc), end):
                return True

        path.pop()
        return False

    if walk(start, end):
        return path
    return []

# Example usage
maze = [
    "#####E#",
    "#     #",
    "#S#####"
]

start = (2, 1)  # Starting point 'S'
end = (0, 5)    # Ending point 'E'

result = pathFind(maze, '#', start, end)
print(result)  # Output: [(2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (0, 5)]
  

  