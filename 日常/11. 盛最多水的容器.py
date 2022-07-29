class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        ans = 0
        while i < j:
            if height[i] < height[j]:
                ans = max(height[i] * (j - i), ans)
                i += 1
            else:
                ans = max(height[j] * (j - i), ans)
                j -= 1
        return ans