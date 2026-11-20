class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        area = 0


        def dfs(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0) or grid[r][c] == 0:
                return 0
            else:
                runningSum = 1
                grid[r][c] = 0
                for dx, dy in directions:
                    runningSum += dfs(r + dx, c + dy)
                return runningSum
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(dfs(r, c), area)
        
        return area