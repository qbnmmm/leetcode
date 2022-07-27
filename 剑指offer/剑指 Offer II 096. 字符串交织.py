class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1), len(s2), len(s3)
        if x + y != z:
            return False

        dp = [[False for _ in range(y + 1)] for _ in range(x + 1)]
        dp[0][0] = True
        for i in range(x + 1):
            for j in range(y + 1):
                if i - 1 >= 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j - 1 >= 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        return dp[x][y]