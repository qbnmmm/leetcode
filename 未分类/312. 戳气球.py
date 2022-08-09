class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]

        # dp[i][j]含义：表示开区间(i, j)内能拿到的最多金币
        dp = [[0] * len(nums) for _ in range(len(nums))]

        def range_best(i: int, j: int) -> None:
            m = 0
            # k是区间内最后一个被戳破的气球
            for k in range(i + 1, j):
                left = dp[i][k]
                right = dp[k][j]
                score = left + nums[i] * nums[k] * nums[j] + right
                if score > m:
                    m = score
            dp[i][j] = m

        # 对每一个区间长度进行循环, 从长度为3开始
        for n in range(2, len(nums)):
            for i in range(len(nums) - n):
                range_best(i, i + n)
        return dp[0][-1]