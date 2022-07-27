class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp_sym = [[False] * n for _ in range(n)]
        dp_mincut = list(range(n))  # 初始化切割次数为切割成单个字符

        # 建立是否为回文串的dp数组
        for i in range(n - 1, -1, -1):  # 从下往上
            dp_sym[i][i] = True  # 单个字母一定是回文串
            for j in range(i + 1, n):  # 从左往右
                if s[i] == s[j]:
                    if j - i == 1 or dp_sym[i + 1][j - 1]:
                        dp_sym[i][j] = True
        # 建立最少切割次数的dp数组
        for i in range(1, n):
            if dp_sym[0][i]:  # 如果0-i自身就是回文串
                dp_mincut[i] = 0
                continue
            for j in range(0, i):  # 对于每个可能的切割位置，如果切割后后面的是回文串，那么切割数为前方切割数+1
                if dp_sym[j + 1][i]:
                    dp_mincut[i] = min(dp_mincut[i], dp_mincut[j] + 1)
        return dp_mincut[-1]
