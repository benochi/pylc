class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        ROWS, COLS = len(mat), len(mat[0])
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q: 
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if(
                    row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or
                    (row,col) in visit
                ): continue
                mat[row][col] = mat[r][c] + 1
                q.append((row, col))
                visit.add((row, col))

        return mat
