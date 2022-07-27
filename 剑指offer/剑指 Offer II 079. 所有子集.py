class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        for num in nums:
            ans += [lst+[num] for lst in ans]
        return ans