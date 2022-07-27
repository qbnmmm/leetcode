class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        depth = len(triangle)
        if depth == 1:
            return triangle[0][0]
        dp = [201 for _ in range(depth)]
        dp[0] = triangle[0][0]
        for i in range(1, depth):
            tmp = dp[0]
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    dp[j] = tmp + triangle[i][j]
                else:
                    left = tmp
                    tmp = dp[j]
                    dp[j] = min(left, dp[j]) + triangle[i][j]
        return min(dp)