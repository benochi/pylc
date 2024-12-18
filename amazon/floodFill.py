class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([(sr, sc)])
        ROWS, COLS = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if(
                    row < 0 or row >= ROWS or
                    col < 0 or col >= COLS or 
                    image[row][col] != originalColor
                ): continue
                q.append((row,col))
        
        return image