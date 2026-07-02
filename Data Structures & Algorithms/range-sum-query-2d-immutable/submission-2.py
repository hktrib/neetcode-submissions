from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # FIX 1: Create a shallow/deep copy so you don't corrupt the original matrix
        self.prefix = [row[:] for row in matrix] 
        
        for i, row in enumerate(self.prefix):
            running = 0
            for j, col in enumerate(row):
                running += col
                self.prefix[i][j] = running

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # FIX 2: Removed the broken `row1 == row2 and col1 == col2` shortcut.
        
        runningSum = 0

        # FIX 3: Use a helper variable for the left boundary.
        # If col1 is 0, we subtract nothing (0). Otherwise, we subtract the index before col1.
        left_bound = col1 - 1 if col1 > 0 else None

        for row in range(row1, row2 + 1):
            if left_bound is not None:
                runningSum += (self.prefix[row][col2] - self.prefix[row][left_bound])
            else:
                runningSum += self.prefix[row][col2]

        return runningSum