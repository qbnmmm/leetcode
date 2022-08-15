from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if target == matrix[i][j]:
                return True
            if target < matrix[i][j]:
                i -= 1
            else:
                j += 1
        return False