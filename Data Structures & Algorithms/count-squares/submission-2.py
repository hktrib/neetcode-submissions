class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        self.points[key] += 1

    def count(self, point: List[int]) -> int:
        qx = point[0]
        qy = point[1]

        count = 0


        for key, value in self.points.items():
            x, y = key[0], key[1]
            if abs(x - qx) == abs(y - qy) and x != qx:
                count += value * self.points[(x, qy)] * self.points[(qx, y)]
        
        return count
