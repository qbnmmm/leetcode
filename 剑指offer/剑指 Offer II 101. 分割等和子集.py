class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        S = sum(nums)
        if S & 1:
            return False
        target = S >> 1
        if max(nums) > target:
            return False

        '''【0/1背包】：从nums中选出的数字刚好能组成target'''
        n = len(nums)

        # 初始化
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # dp[i][j]: 从前i个元素中选出若干个数字刚好能够组成j
        dp[0][0] = True  # 其他 dp[0][j]均为False

        for i in range(1, n + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:  # 容量有限，无法选择第i个数字nums[i-1]
                    dp[i][j] = dp[i - 1][j]
                else:  # 可选择第i个数字nums[i-1]，也可不选
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]

        return dp[n][target]
