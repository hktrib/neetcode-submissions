class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
            
        prev_row = [1, 1]
        new_row = []
        for i in range(2, rowIndex + 1):
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i] + prev_row[i-1])
            
            
            prev_row = [1] + new_row + [1]
            new_row = []
            

        
        return prev_row
