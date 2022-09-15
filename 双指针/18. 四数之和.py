from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        if n == 4 and sum(nums) == target:
            return [nums]
        nums.sort()
        ans = []
        for i in range(n - 3):
            target3 = target - nums[i]
            for j in range(i + 1, n - 2):
                l, r = j + 1, n - 1
                while l < r:
                    tmp = nums[j] + nums[l] + nums[r]
                    if tmp == target3:
                        if [nums[i], nums[j], nums[l], nums[r]] not in ans:
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif tmp < target3:
                        l += 1
                    else:
                        r -= 1
        return ans