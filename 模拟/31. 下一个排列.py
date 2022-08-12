class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            i, j, k = n - 2, n - 1, n - 1

            # 从后向前找第一个相邻升序的元素对(i, j)
            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
                j -= 1

            # 在[j, end)范围内从后向前找第一个满足nums[i] < nums[k]的k。
            while k > j and nums[k] <= nums[i]:
                k -= 1

            # 交换nums[i]和nums[k]，此时[j, end)必然是降序，然后让其翻转形成升序
            if i != -1:
                nums[i], nums[k] = nums[k], nums[i]
                nums[:] = nums[:j] + nums[j:][::-1]

            else:
                nums[:] = nums[::-1]