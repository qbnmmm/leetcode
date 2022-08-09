class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        minn = nums[-1]
        maxx = nums[0]
        begin, end = 0, -1
        for i in range(n):
            if nums[i] < maxx:
                end = i
            else:
                maxx = nums[i]

            if nums[n - i - 1] > minn:
                begin = n - i - 1
            else:
                minn = nums[n - i - 1]
        return end - begin + 1