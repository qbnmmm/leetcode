class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        def toInt(matrix: list[list[str]]) -> list[list[int]]:
            ans = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ans[i][j] = int(matrix[i][j])
            return ans

        m, n = len(matrix), len(matrix[0])
        matrix = toInt(matrix)
        if m > 1:
            for i in range(1, m):
                for j in range(n):
                    if matrix[i][j] != 0:
                        matrix[i][j] += matrix[i - 1][j]
        res = [0] * m
        for height in range(m):
            stack = []
            heights = [0] + matrix[height] + [0]
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    tmp = stack.pop()
                    res[height] = max(res[height], (i - stack[-1] - 1) * heights[tmp])
                stack.append(i)
        return max(res)


a = Solution()
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
ans = a.maximalRectangle(matrix)
print(ans)