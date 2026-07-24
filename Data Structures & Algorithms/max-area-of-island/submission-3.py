class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]

        def dfs(r, c):
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS
                or grid[r][c] == 0):
                return 0
            else:
                area = 1
                grid[r][c] = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    area += dfs(nr, nc)
                return area

        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r, c), maxArea)
        
        return maxArea


