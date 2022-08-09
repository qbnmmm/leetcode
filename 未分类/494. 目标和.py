class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (target + total) & 1:
            return 0
        pos = (total + target) // 2
        neg = (total - target) // 2
        capacity = min(pos, neg)

        # dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        # dp[0][0] = 1
        #
        # for i in range(1, n + 1):
        #     for j in range(capacity + 1):
        #         if j < nums[i]:
        #             dp[i][j] = dp[i - 1][j]
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        # return dp[-1][-1]
        dp = [0] * (capacity + 1)
        dp[0] = 1

        for num in nums:
            for j in range(capacity, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]