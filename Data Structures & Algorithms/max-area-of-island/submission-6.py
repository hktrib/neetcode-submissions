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

        # def dfs(r, c):
        #     if (r >= ROWS or c >= COLS or r < 0 or c < 0) or grid[r][c] == 0:
        #         return 0
        #     else:
        #         runningSum = 1
        #         grid[r][c] = 0
        #         for dx, dy in directions:
        #             runningSum += dfs(r + dx, c + dy)
        #         return runningSum

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            running_sum = 1

            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dx, dy in directions:
                    nr, nc = row + dx, col + dy

                    if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or grid[nr][nc] == 0:
                        continue
                    else:
                        running_sum += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))

            return running_sum
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(bfs(r, c), area)
        
        return area