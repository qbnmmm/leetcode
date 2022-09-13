class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(map(int, list(str(num))))
        maxx = sorted(s, reverse=True)
        m = -1
        mi = -1
        for i in range(len(s)):
            if maxx[i] != s[i]:
                m = maxx[i]
                mi = i
                break
        if m != -1:
            for i in range(len(s) - 1, mi - 1, -1):
                if s[i] == m:
                    s[mi], s[i] = s[i], s[mi]
                    break
        return int("".join(list(map(str, s))))