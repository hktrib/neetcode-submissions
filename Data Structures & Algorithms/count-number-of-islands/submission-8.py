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

        # def dfs(r, c):
        #     if (r >= ROWS or c >= COLS or r < 0 or c < 0) or grid[r][c] == "0":
        #         return
        #     else:
        #         grid[r][c] = "0"
        #         for dx, dy in directions:
        #             dfs(r + dx, c + dy)
        #         return
        #     pass

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dx, dy in directions:
                    nr, nc = row + dx, col + dy
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and \
                        grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count
                