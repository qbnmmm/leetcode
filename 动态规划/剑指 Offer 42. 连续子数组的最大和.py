from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-inf] * n
        dp[0] = nums[0]

        ans = dp[0]

        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
            ans = max(ans, dp[i])
        return ans