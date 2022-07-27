class Solution:
    def maximalRectangle(self, matrix: list[str]) -> int:
        def largestRectangleArea(heights: list[int]) -> int:
            stack = []
            stack.append(0)
            heights.insert(0, 0)
            heights.append(0)
            maxArea = 0
            for i in range(1, len(heights)):
                while heights[stack[-1]] > heights[i]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    maxArea = max(maxArea, height * width)
                stack.append(i)
            return maxArea
        if not matrix:
            return 0
        newMatrix = [[0 for _ in range(len(matrix[0]))]]
        for row in range(len(matrix)):
            rowlist = list(matrix[row])
            rowlist = [int(x) for x in rowlist]
            for i in range(len(rowlist)):
                if newMatrix[row][i] != 0 and rowlist[i] != 0:
                    rowlist[i] += newMatrix[row][i]
            newMatrix.append(rowlist)
        maxArea = 0
        for i in range(1, len(newMatrix)):
            maxArea = max(maxArea, largestRectangleArea(newMatrix[i]))
        return maxArea

matrix = ["01","10"]
a = Solution()
ans = a.maximalRectangle(matrix)
print(ans)