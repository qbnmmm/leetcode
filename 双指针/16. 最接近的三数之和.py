from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 3:
            return sum(nums)
        ans = 10000000
        ret = 10000000
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            tgt = target - nums[i]
            while l < r:
                diff = tgt - nums[l] - nums[r]
                if abs(diff) < ans:
                    ans = abs(diff)
                    ret = nums[i] + nums[l] + nums[r]
                if diff < 0:
                    r -= 1
                elif diff > 0:
                    l += 1
                else:
                    return target
        return ret