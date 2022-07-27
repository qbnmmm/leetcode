class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            ret = 1
            vis[i][j] = True
            if i > 0 and grid[i - 1][j] == 1 and not vis[i - 1][j]:  # up
                ret += dfs(i - 1, j)
            if i < m - 1 and grid[i + 1][j] == 1 and not vis[i + 1][j]:  # down
                ret += dfs(i + 1, j)
            if j > 0 and grid[i][j - 1] == 1 and not vis[i][j - 1]:  # left
                ret += dfs(i, j - 1)
            if j < n - 1 and grid[i][j + 1] == 1 and not vis[i][j + 1]:  # right
                ret += dfs(i, j + 1)
            return ret

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans


grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]
a = Solution()
ans = a.maxAreaOfIsland(grid)
print(ans)
