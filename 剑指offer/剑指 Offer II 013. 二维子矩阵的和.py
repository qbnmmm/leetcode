class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.sumMatrix = []
        row = len(matrix)  # 行数
        col = len(matrix[0])  # 列数
        for m in range(row):
            tempRow = []
            tempSum = 0
            for n in range(col):
                tempSum += matrix[m][n]
                if m > 0:
                    tempSum += self.sumMatrix[m - 1][n]
                    if n > 0:
                        tempSum -= self.sumMatrix[m - 1][n - 1]
                tempRow.append(tempSum)
            self.sumMatrix.append(tempRow)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.sumMatrix[row2][col2]
        flagRow, flagCow = row1 > 0, col1 > 0  # 左、上边界可能为0,True表示非边界
        if flagRow:
            ans -= self.sumMatrix[row1 - 1][col2]
        if flagCow:
            ans -= self.sumMatrix[row2][col1 - 1]
        if flagCow and flagRow:
            ans += self.sumMatrix[row1 - 1][col1 - 1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
a = NumMatrix(matrix)
b = a.sumRegion(2, 1, 4, 3)
print(b)
