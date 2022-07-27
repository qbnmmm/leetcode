import sys


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        MIN = -sys.maxsize - 1
        f = [[[MIN] * n for _ in range(n)] for _ in range(n * 2 - 1)]
        f[0][0][0] = grid[0][0]
        for k in range(1, n * 2 - 1):
            for x1 in range(max(k - n + 1, 0), min(k + 1, n)):
                y1 = k - x1
                if grid[x1][y1] == -1:
                    continue
                for x2 in range(x1, min(k + 1, n)):
                    y2 = k - x2
                    if grid[x2][y2] == -1:
                        continue
                    res = f[k - 1][x1][x2]
                    if x1:
                        res = max(res, f[k - 1][x1 - 1][x2])
                    if x2:
                        res = max(res, f[k - 1][x1][x2 - 1])
                    if x1 and x2:
                        res = max(res, f[k - 1][x1 - 1][x2 - 1])
                    res += grid[x1][y1]
                    if x2 != x1:
                        res += grid[x2][y2]
                    f[k][x1][x2] = res
        return max(f[-1][-1][-1], 0)


grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
a = Solution()
ans = a.cherryPickup(grid)
print(ans)
