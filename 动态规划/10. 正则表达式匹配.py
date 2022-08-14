class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1

        # dp[i][j]表示s的前i个字符和p的前j个字符能否匹配
        dp = [[False] * n for _ in range(m)]

        # 初始化，s此时为空字符串
        dp[0][0] = True  # 空字符串
        for j in range(2, n, 2):  # p的偶数位为*则能匹配
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        '''
        p[i - 1]为'*'时，dp[i][j]为以下任意情况则为True：
            1、dp[i][j - 2]:将字符串组合p[j - 2]*看作出现0次，能否匹配;
            2、dp[i - 1][j] and s[i - 1] == p[j - 2]:让字符p[j - 2]多出现一次，能否匹配；
            3、dp[i - 1][j] and p[j - 2] == '.':让字符'.'多出现一次，能否匹配。
        p[j - 1]不为'*'时，dp[i][j]为以下任意情况则为True：
            1、dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:字符串 s 的前 i-1 个字符和 p 的前 j -1个字符匹配, 且s的第i个字符等于p的第j个字符；
            2、dp[i - 1][j - 1] and p[i - ] == '.':字符串 s 的前 i-1 个字符和 p 的前 j -1个字符匹配, 且p的第j个字符为'.'。
        '''
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') \
                    if p[j - 1] == '*' else \
                    dp[i - 1][j - 1] and (p[j - 1] == '.' or s[i - 1] == p[j - 1])
        return dp[-1][-1]
