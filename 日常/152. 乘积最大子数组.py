class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp_min = [0] * n
        dp[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp[i - 1] * nums[i], dp_min[i - 1] * nums[i])
        return max(max(dp), max(dp_min))