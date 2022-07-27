class Solution:
    def __init__(self):
        self.ans = 0

    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        vis = [False for _ in range(n)]

        def dfs(idx: int, lenth: int):
            if vis[idx]:
                self.ans = max(self.ans, lenth)
                return
            vis[idx] = True
            dfs(nums[idx], lenth + 1)
        for i in range(n):
            dfs(i, 0)
        return self.ans


A = [5, 4, 0, 3, 1, 6, 2]
a = Solution()
ans = a.arrayNesting(A)
print(ans)
