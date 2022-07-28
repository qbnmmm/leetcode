class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]