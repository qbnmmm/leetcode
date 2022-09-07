class Solution:
    def __init__(self):
        self.ans = 0
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set()

        def isValid(i: int, j: int) -> bool:
            if 0 <= i < m and 0 <= j < n and (i, j) not in vis:
                tmpi, tmpj = i, j
                calc = 0
                while tmpi != 0:
                    calc += tmpi % 10
                    tmpi //= 10
                while tmpj != 0:
                    calc += tmpj % 10
                    tmpj //= 10
                return calc <= k
            return False

        def dfs(i: int, j: int):
            if not isValid(i, j):
                return
            self.ans += 1
            vis.add((i, j))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + di, j + dj)

        dfs(0, 0)
        return self.ans