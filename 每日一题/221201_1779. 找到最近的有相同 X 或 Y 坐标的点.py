from functools import lru_cache
from typing import List


class Solution:
    @lru_cache
    def calc_dis(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)

    def valid(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        return x1 == x2 or y1 == y2

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        nearest = 1000000
        ans = -1
        n = len(points)
        for i in range(n):
            x2, y2 = points[i]
            if self.valid(x, y, x2, y2) and self.calc_dis(x, y, x2, y2) < nearest:
                nearest = self.calc_dis(x, y, x2, y2)
                ans = i
        return ans