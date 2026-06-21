class Solution:
    def isPathCrossing(self, path: str) -> bool:
        y = 0
        x = 0

        visit = set()

        for p in path:
            visit.add((x, y))
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in visit:
                return True

        return False
            
        