class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        for i in range(2, n):
            a = nums[i - 2]
            b = nums[i - 3] if i > 2 else 0
            nums[i] += max(a, b)
        return max(nums[-1], nums[-2])
