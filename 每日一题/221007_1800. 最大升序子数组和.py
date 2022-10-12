class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curm, curs, ans = nums[0], nums[0], nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > curm:
                curm = nums[i]
                curs += nums[i]
                if curs > ans:
                    ans = curs
            else:
                curs = curm = nums[i]
        return ans