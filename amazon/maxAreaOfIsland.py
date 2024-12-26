class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
                    area = 0

                    while q:
                        curr_r, curr_c = q.popleft()
                        area += 1
                        for dr, dc in directions:
                            row, col = dr + curr_r, dc + curr_c
                            if(
                                row < 0 or row >= ROWS or
                                col < 0 or col >= COLS or
                                (row, col) in visit or
                                grid[row][col] == 0
                            ): continue
                            q.append((row, col))
                            visit.add((row, col))
                    maxArea = max(area, maxArea)
        
        return maxArea