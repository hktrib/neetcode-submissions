class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = [[False] * COLS for _ in range(ROWS)]
        perimeter = 0

        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]

        def dfs(row, col):
            nonlocal perimeter
            if visited[row][col]:
                return
            else:
                visited[row][col] = True
                for dr, dc in directions:
                    newDR = row + dr
                    newDC = col + dc

                    if newDR >= ROWS or newDC >= COLS \
                        or newDR < 0 or newDC < 0 \
                        or grid[newDR][newDC] == 0:
                        perimeter += 1
                    else:
                        dfs(newDR, newDC)
                
                print(perimeter)
            pass 

            
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col)
                    break
        return perimeter
                    
        

