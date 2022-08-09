class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i >> 1]
        return dp