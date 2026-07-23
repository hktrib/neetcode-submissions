class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS 
                or grid[r][c] == 0):
                return 1
            elif (r, c) in visited:
                return 0
            else:
                visited.add((r, c))

                currPerm = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    currPerm += dfs(nr, nc)

                return currPerm
            pass

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
