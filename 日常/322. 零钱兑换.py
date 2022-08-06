# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         n = len(coins)
#         # dp[i][j]从前i种硬币中组成金额j所需最少数量
#         dp = [[amount + 1] * (amount + 1) for _ in range(n + 1)]
#         dp[0][0] = 0
#
#         for i in range(1, n + 1):  # 遍历硬币
#             for j in range(amount + 1):  # 遍历背包
#                 if j < coins[i - 1]:  # 容量有限，无法装下该面值的硬币
#                     dp[i][j] = dp[i - 1][j]
#                 else:
#                     # 遍历背包的实质是背包容量在不断增加，随着背包容量增大，
#                     # 当前硬币可能会多放一枚进背包，那么放进一枚后总的金币数
#                     # 就应该是dp[i][j - coin[i - 1]] + 1
#                     # 其中j - coin[i - 1]意思是，因为放了这枚金币而让金额j目标
#                     # 减少了coin[i - 1]
#                     dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
#         ans = dp[-1][-1]
#         return ans if ans != amount + 1 else -1


# 滚动数组，优化空间复杂度
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp2 = [amount + 1] * (amount + 1)
            for j in range(amount + 1):
                if j < coins[i - 1]:
                    dp2[j] = dp[j]
                else:
                    dp2[j] = min(dp[j], dp2[j - coins[i - 1]] + 1)
            dp = dp2
        ans = dp[-1]
        return ans if ans != amount + 1 else -1


coins = [1, 2, 5]
amount = 100
a = Solution()
ans = a.coinChange(coins, amount)
print(ans)