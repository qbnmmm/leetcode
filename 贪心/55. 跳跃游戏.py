from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0  # 当前能到达的最远位置
        for i, jump in enumerate(nums):  # i为当前位置，jump为跳数
            if i + jump > max_i >= i:  # 如果当前位置能到达且跳数大于能达到的最远位置，就更新max_i
                max_i = i + jump
        return max_i >= i

nums = [1, 2, 3]
a = Solution()
ans = a.canJump(nums)
print(ans)
