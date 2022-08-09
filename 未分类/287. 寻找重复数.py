class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        dic = [0] * n
        i = 0
        while True:
            dic[nums[i]] += 1
            if dic[nums[i]] == 2:
                return nums[i]
            i = nums[i]
