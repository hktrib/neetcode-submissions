class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        count = 0

        def dfs(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0) or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                for dx, dy in directions:
                    dfs(r + dx, c + dy)
                return
            pass

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count
                