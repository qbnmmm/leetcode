class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idxs = {}
        ans = -1
        for i, c in enumerate(s):
            idxs[c] = idxs[c] if c in idxs else i
            ans = max(ans, i - idxs[c] - 1)
        return ans