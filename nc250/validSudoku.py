class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        grids = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                    
                if (r, val) in rows or (c, val) in cols or (r // 3, c // 3, val) in grids:
                    return False

                rows.add((r, val))
                cols.add((c, val))
                grids.add((r // 3, c // 3, val))
        
        return True