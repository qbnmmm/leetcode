class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] 表示word1的前i个字符和word2的前j个字符的距离
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化：任意空字符串与另一个单词的距离
        for i in range(1, n + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1

        '''
        状态转移：
        增:dp[i][j] = dp[i][j - 1] + 1
        删:dp[i][j] = dp[i - 1][j] + 1
        改:dp[i][j] = dp[i - 1][j - 1] + 1
        取三种方式的最小值
        '''
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]