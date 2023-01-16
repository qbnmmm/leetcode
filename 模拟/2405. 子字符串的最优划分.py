class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        tmp = set()
        for c in s:
            if c not in tmp:
                tmp.add(c)
            else:
                ans += 1
                tmp.clear()
                tmp.add(c)
        return ans