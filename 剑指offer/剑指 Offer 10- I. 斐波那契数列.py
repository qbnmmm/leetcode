class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        mod = 1000000007
        i = 3
        while i <= n:
            dp[i % 3] = dp[(i - 1) % 3] % mod + dp[(i - 2) % 3] % mod
            i += 1
        return dp[(i - 1) % 3] % mod


n = 5
a = Solution()
ans = a.fib(n)
print(ans)
