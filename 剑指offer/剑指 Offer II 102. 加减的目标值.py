class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:  # target可能为负
            return 0
        if (total + target) & 1:  # 不能被2整除【对应于pos不是整数】
            return 0

        '''【0/1背包】：从nums中选出数字组成pos或neg'''
        pos = (total + target) >> 1
        neg = (total - target) >> 1
        capcity = min(pos, neg)  # 取pos和neg中的较小者，以使得dp空间最小
        n = len(nums)

        # 初始化
        dp = [[0] * (capcity + 1) for _ in range(n + 1)]
        # dp[i][j]: 从前i个元素中选出若干个其和为j的方案数
        dp[0][0] = 1  # 其他 dp[0][j]均为0

        # 状态更新
        for i in range(1, n + 1):
            for j in range(capcity + 1):
                if j < nums[i - 1]:  # 容量有限，无法选择第i个数字nums[i-1]
                    dp[i][j] = dp[i - 1][j]
                else:  # 可选择第i个数字nums[i-1]，也可不选【两种方式之和】
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        return dp[n][capcity]
