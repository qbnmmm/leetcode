class Solution:
    def rob(self, nums: list[int]) -> int:
        nums = [0, 0, 0] + nums[:]
        n = len(nums)
        dp = [0] * n
        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        return max(dp[-1], dp[-2])