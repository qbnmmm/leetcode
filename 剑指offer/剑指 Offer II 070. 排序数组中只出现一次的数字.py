class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                break
            i += 2
        return nums[i]