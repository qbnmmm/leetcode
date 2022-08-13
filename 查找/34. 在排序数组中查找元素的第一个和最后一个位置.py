class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearchLeft(nums: list[int], target: int) -> int:
            l, r = -1, len(nums)
            while l + 1 != r:
                m = (l + r) >> 1
                if nums[m] >= target:
                    r = m
                else:
                    l = m
            return r

        def binarySearchRight(nums: list[int], target: int) -> int:
            l, r = -1, len(nums)
            while l + 1 != r:
                m = (l + r) >> 1
                if nums[m] <= target:
                    l = m
                else:
                    r = m
            return l

        indexLeft = binarySearchLeft(nums, target)
        indexRight = binarySearchRight(nums, target)
        '''
        红蓝染色法如何查找不存在的元素？
        因为红蓝染色法一定会返回结果，
        因此需要判断结果索引的值是否等于答案
        
        另外需要判断全染成一个颜色后的返回值是否合法：
        如果全染成一个颜色，说明target可能大于/小于nums中的所有元素
        此时indexLeft和indexRight可能会在一边，并且出现类似于Left> n >Right的情况
        所以需要加上一个indexLeft <= indexRight的判断
        '''
        if indexLeft <= indexRight and nums[indexRight] == nums[indexLeft] == target:
            return [indexLeft, indexRight]
        return [-1, -1]


a = Solution()
nums = [2, 2]
ans = a.searchRange(nums, 3)
print(ans)
