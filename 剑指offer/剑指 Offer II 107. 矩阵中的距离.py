import collections


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        vis = [[False] * n for _ in range(m)]
        stack = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    stack.append((i, j, 0))
                    vis[i][j] = True

        while stack:
            i, j, k = stack.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                    stack.append((x, y, k + 1))
                    vis[x][y] = True
                    ans[x][y] = k + 1

        return ans


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
a = Solution()
ans = a.updateMatrix(mat)
print(ans)
