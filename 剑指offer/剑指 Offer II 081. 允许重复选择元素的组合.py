class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backTracking(index: int, path: list[int], target: int) -> None:
            if index >= len(candidates) or target < 0:
                return
            if target == 0:# 收集条件
                ans.append(path[:])
            for i in range(index, len(candidates)):# 注意可以重复收集
                path.append(candidates[i]) # 做选择
                backTracking(i, path, target - candidates[i])
                path.pop()# 取消选择

        ans = []
        path = []
        candidates.sort()
        # 收集逻辑为target == 0

        backTracking(0, path, target)
        return ans
