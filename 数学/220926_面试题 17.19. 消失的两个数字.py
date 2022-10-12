from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        cur = n * (1 + n) // 2 - sum(nums)  # cur表示缺失两值之和
        total, t = cur, cur // 2
        cur = t * (1 + t) // 2 - sum([x for x in nums if x <= t])  # 理论总和减去实际总和得到缺失的其中一个
        return [cur, total - cur]
