class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backTracking(cur_sum: int, index: int) -> None:
            if cur_sum == target:
                ans.append(path[:])
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    if cur_sum + candidates[i] > target:
                        break
                    else:
                        path.append(candidates[i])
                        backTracking(cur_sum + candidates[i], i + 1)
                        path.pop()

        ans, path = [], []
        candidates.sort()
        backTracking(0, 0)
        return ans
