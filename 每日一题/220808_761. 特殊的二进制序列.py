class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cur = last = 0
        candidates = []
        for i, c in enumerate(s):
            cur += 1 if c == '1' else -1
            if not cur:
                candidates.append('1' + self.makeLargestSpecial(s[last + 1:i]) + '0')
                last = i + 1
        return ''.join(sorted(candidates, reverse=True))