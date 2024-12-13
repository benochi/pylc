class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        q = deque([(0,0)])
        length = 1
        ROWS, COLS = len(grid), len(grid[0])
        visit = set((0,0))

        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if (r,c) == (ROWS -1, COLS -1):
                    return length
                for dr, dc in directions:
                    row,col = dr + r, dc + c
                    if (row >= ROWS or row < 0 or 
                        col >= COLS or col < 0 or
                        (row,col) in visit or
                        grid[row][col] == 1
                        ): 
                        continue
                    q.append((row,col))
                    visit.add((row,col))
            length += 1
            
        return -1