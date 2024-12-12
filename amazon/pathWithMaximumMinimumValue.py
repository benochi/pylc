from collections import deque
from typing import List

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def can_reach_end(min_val):
            # Use max heap to prioritize paths with higher minimum values
            heap = [(-grid[0][0], 0, 0)]
            visited = set([(0, 0)])
            
            while heap:
                path_min, r, c = heappop(heap)
                path_min = -path_min  # Convert back to positive
                
                # If we've reached the end and path minimum is at least min_val
                if (r, c) == (ROWS - 1, COLS - 1):
                    return path_min >= min_val
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # Check grid bounds and not previously visited
                    if (0 <= row < ROWS and 0 <= col < COLS and 
                        (row, col) not in visited):
                        
                        # Take the minimum of current path and new cell
                        new_path_min = min(path_min, grid[row][col])
                        
                        # Only add to heap if it meets the minimum requirement
                        if new_path_min >= min_val:
                            heappush(heap, (-new_path_min, row, col))
                            visited.add((row, col))
            
            return False
        
        # Binary search for maximum possible minimum path value
        low, high = 0, min(grid[0][0], grid[-1][-1])
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_reach_end(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result
