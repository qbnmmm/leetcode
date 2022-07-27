class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dic = {i: [] for i in range(n)}
        for c in range(2 * n - 1):
            l = c // 2
            r = l + c % 2
            while l >= 0 and r < n and s[l] == s[r]:
                dic[l].append(r)
                l -= 1
                r += 1

        ans = []
        path = []

        def backtrace(l: int) -> None:
            if l == n:
                ans.append(path[:])
                return
            for r in dic[l]:
                path.append(s[l:r + 1])
                backtrace(r+1)
                path.pop()
        backtrace(0)
        return ans
