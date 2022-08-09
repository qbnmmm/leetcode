class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def isValid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n
        i, j = m - 1, 0
        while True:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur < target:
                if not isValid(i, j + 1):
                    return False
                j += 1
            else:
                if not isValid(i - 1, j):
                    return False
                i -= 1
