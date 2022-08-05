class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 找到第一个0
        first_zero = 0
        while first_zero < n:
            if nums[first_zero] == 0:
                break
            first_zero += 1

        # 快指针遇到非0就把它和第一个0交换
        r = first_zero
        while r < n:
            if nums[r] != 0:
                nums[first_zero], nums[r] = nums[r], nums[first_zero]
                first_zero += 1
            r += 1
        return


nums = [1]
a = Solution()
ans = a.moveZeroes(nums)
print(ans)