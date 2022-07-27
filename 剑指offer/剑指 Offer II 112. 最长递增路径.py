class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)] # 存储访问过的单元格走到最长递增路径
        ret = 0
        def isLegal(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n

        def dfs(row: int, col: int) -> int:
            if res[row][col] != 0: # res中已经存储了该单元的最长递增路径
                return res[row][col]
            ans = 1
            cur = matrix[row][col]
            if isLegal(row - 1, col) and matrix[row - 1][col] > cur: # up
                ans = max(ans, dfs(row - 1, col) + 1)
            if isLegal(row + 1, col) and matrix[row + 1][col] > cur:  # down
                ans = max(ans, dfs(row + 1, col) + 1)
            if isLegal(row, col - 1) and matrix[row][col - 1] > cur: # left
                ans = max(ans, dfs(row, col - 1) + 1)
            if isLegal(row, col + 1) and matrix[row][col + 1] > cur: # right
                ans = max(ans, dfs(row, col + 1) + 1)
            res[row][col] = ans
            return ans

        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i, j))
        return ret

a = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
ans = a.longestIncreasingPath(matrix)
print(ans)
