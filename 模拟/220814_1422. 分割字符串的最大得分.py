class Solution:
    def maxScore(self, s: str) -> int:
        left = right = 0
        n = len(s)
        sl, sr = [0] * n, [0] * n
        for l in range(n):
            r = n - l - 1
            left += 1 if s[l] == '0' else 0
            right += 1 if s[r] == '1' else 0
            sl[l] = left
            sr[r] = right
        ans = 0
        for i in range(n - 1):
            score = sl[i] + sr[i + 1]
            ans = max(ans, score)
        return ans