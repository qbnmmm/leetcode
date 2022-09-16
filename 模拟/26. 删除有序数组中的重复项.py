from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        vis = set()
        while i < len(nums):
            if nums[i] not in vis:
                vis.add(nums[i])
                i += 1
            else:
                del nums[i]
        return len(nums)