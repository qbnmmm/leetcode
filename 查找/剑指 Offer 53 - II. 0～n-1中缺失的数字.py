class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1 - nums[0]
        l, r = -1, n
        while l + 1 != r:
            mid = (l + r) >> 1
            if mid == nums[mid]:
                l = mid
            else:
                r = mid
        if l == -1:
            return nums[r] - 1
        return nums[l] + 1