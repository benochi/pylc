def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #handle setup rows, cols, visit
        rows, cols = len(grid), len(grid[0])
        visit = set() #take (r,c) tuples

        # handle DFS
        def dfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or
                grid[r][c] == 0 or (r,c) in visit):
                return 0
            
            visit.add((r,c))
            return (1 + dfs(r+1,c) +
                        dfs(r-1,c) +
                        dfs(r,c+1) +
                        dfs(r,c -1)) 
            
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area