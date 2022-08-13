class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        m, n = len(s), len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                break
        return s[i + 1:] == t[j:] or s[i:] == t[j + 1:] or s[i + 1:] == t[j + 1:]