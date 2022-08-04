class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        def isValid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not vis[x][y]

        def dfs(x: int, y: int) -> None:
            vis[x][y] = True
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if isValid(nx, ny):
                    dfs(nx, ny)

        ans = 0

        for i in range(m):
            for j in range(n):
                if isValid(i, j):
                    dfs(i, j)
                    ans += 1
        return ans