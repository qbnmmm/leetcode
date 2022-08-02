class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)

        def backTrace(path: list[int]):
            if len(path) == n:
                ans.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backTrace(path)
                path.pop()

        backTrace([])
        return ans