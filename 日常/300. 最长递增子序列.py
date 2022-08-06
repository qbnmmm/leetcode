class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        tails, ans = [0] * n, 0
        for num in nums:
            i, j = 0, ans
            while i < j:
                m = (i + j) >> 1
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == ans:
                ans += 1
        return ans
