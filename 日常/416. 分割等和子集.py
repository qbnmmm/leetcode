# https://leetcode.cn/problems/partition-equal-subset-sum/solution/416-fen-ge-deng-he-zi-ji-dong-tai-gui-hu-csk5/
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sumAll = sum(nums)
        if sumAll & 1:
            return False
        target = sumAll >> 1
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]