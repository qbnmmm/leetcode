from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # 统计和为1的行与和为1的列
        rows, cols = [], []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            if sum(mat[i]) == 1:
                rows.append(i)
        for j in range(n):
            s = 0
            for i in range(m):
                s += mat[i][j]
            if s == 1:
                cols.append(j)

        ans = 0
        # 如果行列交叉为1则为特殊位置
        for row in rows:
            for col in cols:
                if mat[row][col] == 1:
                    ans += 1
        return ans