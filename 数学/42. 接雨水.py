class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        ans = 0
        left = right = 0  # left随着height的增大而增大，从左到右，right相反

        # ans在循环后表示两次雨水面积加一次其他面积
        # 其他面积包括黑块面积和高为最高点的矩形的空白部分，本来黑块也会累两次，但是在循环里去掉了
        for i in range(n):
            left = max(left, height[i])
            right = max(right, height[-i - 1])
            ans += left + right - height[i] # 减去一次黑块面积
        return ans - left * n  # 在返回值处减去一次矩形面积，就只剩下答案了