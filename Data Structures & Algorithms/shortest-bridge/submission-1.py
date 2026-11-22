class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            [1, 0],
            [0, 1],
            [0, -1],
            [-1, 0]
        ]

        queue = deque()

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == -1 or grid[r][c] == 0:
                return 
            else:
                grid[r][c] = -1
                queue.append((r, c))

                for dx, dy in directions:
                    dfs(r + dx, c + dy)

        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        level = 1
        while queue:
            # snapshot the level 
            print(f"q: {queue}")


            print(f"level: {level}")
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or grid[nr][nc] == -1:
                        continue
                    else:
                        if grid[nr][nc] == 1:
                            return level - 1
                        else:
                            grid[nr][nc] = -1
                            queue.append((nr, nc))
            level += 1
        return level - 1
        
