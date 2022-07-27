class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        n = len(position)
        if n == 1:
            return 0
        res = [0, 0]
        for i in range(n):
            res[position[i] % 2] += 1
        return min(res)
