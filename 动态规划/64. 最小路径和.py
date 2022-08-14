class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]  # dp[i][j]表示从起点到（i, j)的最小路径和
        dp[0][0] = grid[0][0]

        # 初始化：第一行和第一列
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 当前格子只会从上方和左方到达，进一步降低空间复杂度可以用滚动数组
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]