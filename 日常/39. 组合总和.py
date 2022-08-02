class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []

        def backTrack(target: int, path: list):
            if target == 0:
                ans.append(path[:])
                return
            for num in candidates:
                if path and num < path[-1]: continue
                if num <= target:
                    path.append(num)
                    backTrack(target - num, path)
                    path.pop()
                else:
                    continue

        backTrack(target, [])
        return ans


nums = [2, 3, 6, 7]
a = Solution()
ans = a.combinationSum(nums, 7)
print(ans)