class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            dp[i + 1] = dp[i]
            if int(num_str[i - 1:i + 1]) < 26 and num_str[i - 1] != '0':
                dp[i + 1] += dp[i - 1]
        return dp[-1]