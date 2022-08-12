class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp[i]表示以s[i]为结尾的字符串的最长有效括号
        maxVal = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':  # 如果前一个字符就是（，则直接给dp+2
                    dp[i] = 2
                    if i - 2 >= 0:  # 在+2操作后如果dp[i - 2]不为0，同样也是有效的，需要加上
                        dp[i] += dp[i - 2]
                elif dp[i - 1] > 0:  # 当前字符为），且前一个字符是有效的，需要考虑是否有嵌套
                    # 如果有嵌套的有效括号，则当前的）对应的所在位置应该是i - dp[i - 1] - 1，且此位置应该是一个（
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] += dp[i - dp[i - 1] - 2]
            maxVal = max(maxVal, dp[i])
        return maxVal
