class Solution:
    def findRepeatNumber(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        """
        因为有重复元素的存在，所以可以将所有值放在对应下标，当出现冲突时就可以返回
        """
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]