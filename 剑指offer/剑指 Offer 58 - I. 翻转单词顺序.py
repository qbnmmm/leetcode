class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        if not words:
            return ""
        ans = ""
        for i in range(len(words) - 1, 0, -1):
            ans += words[i] + ' '
        ans += words[0]
        return ans