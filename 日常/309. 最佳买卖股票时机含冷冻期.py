from math import inf


# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         if n == 1:
#             return 0
#         dp = [[0] * 3 for _ in range(n)]
#         '''
#         dp[i][0]表示第i天结束时，手上无股票且处于非冷冻期的最大利润
#         dp[i][1]表示第i天结束时，手上持有股票时的最大利润
#         dp[i][2]表示第i天结束时，手上无股票且处于冷冻期的最大利润
#         '''
#         dp[0][0] = 0
#         dp[0][1] = -prices[0]
#         dp[0][2] = -inf
#         for i in range(1, n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])  # 昨天没有交易
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])  # 昨天持有股票或者昨天刚买入股票
#             dp[i][2] = dp[i - 1][1] + prices[i]  # 今天卖掉持有的股票
#
#         return max(dp[-1][0], dp[-1][2])

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp0, dp1, dp2 = 0, -prices[0], -inf
        for i in range(1, n):
            dp0, dp1, dp2 = max(dp0, dp2), max(dp1, dp0 - prices[i]), dp1 + prices[i]
        return max(dp0, dp2)