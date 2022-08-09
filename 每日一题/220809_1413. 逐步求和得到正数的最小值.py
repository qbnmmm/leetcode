from math import inf


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        minn = inf
        presum = 0
        for num in nums:
            presum += num
            if presum < minn:
                minn = presum
        return max(1 - minn, 1)