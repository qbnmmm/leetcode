class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]