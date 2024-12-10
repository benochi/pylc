from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize variables to keep track of time and grid dimensions
        num_minutes = 0
        m, n = len(grid), len(grid[0])  # m = number of rows, n = number of columns
        
        # Define constants for cell states
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        
        # Initialize a queue to perform BFS and a counter for fresh oranges
        queue = deque()
        num_fresh = 0
        
        # Traverse the grid to enqueue all initially rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))  # Add position of rotten orange to queue
                elif grid[i][j] == FRESH:
                    num_fresh += 1  # Count fresh oranges
        
        # If there are no fresh oranges, no time is needed
        if num_fresh == 0:
            return 0
        
        # Define the directions for adjacent cells (up, down, left, right)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        # Perform BFS to rot adjacent fresh oranges
        while queue:
            num_minutes += 1  # Increment time at each level of BFS
            for _ in range(len(queue)):  # Process all oranges that are rotten at this minute
                i, j = queue.popleft()  # Get the position of the current rotten orange
                for di, dj in directions:
                    r, c = i + di, j + dj  # Calculate adjacent cell positions
                    # Check if the adjacent cell is within grid bounds and has a fresh orange
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN  # Rot the fresh orange
                        num_fresh -= 1  # Decrement the count of fresh oranges
                        queue.append((r, c))  # Add the newly rotten orange to the queue
        
        # After BFS, check if there are any fresh oranges left
        if num_fresh > 0:
            return -1  # Impossible to rot all oranges
        else:
            return num_minutes  # All oranges rotted successfully
