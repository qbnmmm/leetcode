from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        l, r = 0, n - 1
        while l < r:
            if nums[l] & 1:
                l += 1
                continue
            if not nums[r] & 1:
                r -= 1
                continue
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
