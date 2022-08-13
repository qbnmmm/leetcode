class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums: return 0
        n = len(nums)

        # 二分查找左边界
        l, r = -1, n
        while l + 1 != r:
            mid = (l + r) >> 1
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if r == n or nums[r] != target:  # 不存在target
            return 0
        left = l

        # 二分查找右边界
        l, r = -1, n
        while l + 1 != r:
            mid = (l + r) >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        right = l
        return right - left
