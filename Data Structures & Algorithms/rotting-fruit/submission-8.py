class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            [1, 0],
            [0, 1],
            [0, -1],
            [-1, 0]
        ]

        def bfs(q, fresh_fruits) -> int:
            minutes = 0

            while q:

                print(f"q: {q}")
                print(f"fresh_fruits: {fresh_fruits}")
                print(f"minutes: {minutes}")
                # snapshot current length of the queue
                if fresh_fruits == 0:
                    break
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        # check in bound, and not 0 or 2
                        # then we mark it 2 and put on the queue

                        if (0 <= nr < ROWS) and (0 <= nc < COLS) and \
                            (grid[nr][nc] != 0 and grid[nr][nc] != 2):
                            fresh_fruits -= 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                        else:
                            continue
                minutes += 1
            return minutes if fresh_fruits == 0 else -1


        queue = deque()
        fresh_fruits = 0

        # grab all the rotten fruits and put into the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        return bfs(queue, fresh_fruits)
        
