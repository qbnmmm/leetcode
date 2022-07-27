class Solution:
    def nextNum(self, n: int, pos: int) -> int:
        s = list(str(n))
        for i in range(len(s) - 1, pos - 1, -1):
            if s[i] > s[pos]:
                s[i], s[pos] = s[pos], s[i]
                break
        b = sorted(s[pos + 1:])
        s = s[:pos + 1]
        s = s + b
        ans = ''.join(s)
        return int(ans)

    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        pos = -1
        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                pos = i
                break
        if pos == -1:
            return -1
        ans = self.nextNum(n, pos)
        return ans if ans < 2 ** 31 else -1
