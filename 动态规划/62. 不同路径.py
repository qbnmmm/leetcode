class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1 or n == 1:
            return 1

        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
