class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return nums
        nums.sort(reverse=True)
        l, r = -1, n
        l_sum, r_sum = 0, 0
        while l + 1 != r:
            if l_sum <= r_sum:
                l += 1
                l_sum += nums[l]
            else:
                r -= 1
                r_sum += nums[r]
        if l_sum <= r_sum:
            return nums[:l + 2]
        else:
            return nums[:l + 1]