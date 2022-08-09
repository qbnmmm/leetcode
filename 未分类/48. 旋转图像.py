class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n >> 1): # 上下翻转
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n): # 以主对角线为轴翻转
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]