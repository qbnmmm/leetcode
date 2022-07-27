class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        stack.append(0)
        heights.insert(0, 0)
        heights.append(0)
        maxArea = 0
        for i in range(1,len(heights)):
            while heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
