class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        ans = n
        while left <= right:
            mid = (right + left) >> 1
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


a = Solution()
nums = [1, 3, 5, 6]
target = 5
ans = a.searchInsert(nums, target)
print(ans)