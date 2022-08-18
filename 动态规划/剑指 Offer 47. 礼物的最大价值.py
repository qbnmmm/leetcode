from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return grid[0][0]
        dp0 = [0] * n
        dp1 = [0] * n

        dp0[0] = grid[0][0]
        for i in range(1, n):
            dp0[i] = dp0[i - 1] + grid[0][i]

        for i in range(1, m):
            dp1[0] = dp0[0] + grid[i][0]
            for j in range(1, n):
                dp1[j] = max(dp0[j], dp1[j - 1]) + grid[i][j]
            dp0, dp1 = dp1, dp0
        return dp0[-1]
