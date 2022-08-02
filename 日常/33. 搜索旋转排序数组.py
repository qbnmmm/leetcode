class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:  # 左边比中间小，说明断崖出现在右边
                if nums[left] <= target <= nums[mid]:  # 如果target出现在左半侧就不需要考虑断崖了
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 断崖出现在左边
                if nums[mid] <= target <= nums[right]:  # target在右边
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
