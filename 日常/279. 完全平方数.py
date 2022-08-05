from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            minn = inf
            j = 1
            while j * j <= i:
                minn = min(minn, dp[i - j * j])
                j += 1
            dp[i] = minn + 1
        return dp[-1]