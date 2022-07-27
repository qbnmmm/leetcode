class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for indice in indices:
            rows[indice[0]] += 1
            cols[indice[1]] += 1
        ans = 0
        len = 0
        for i in range(m):
            if rows[i] & 1:
                len += 1
                ans += n
        for i in range(n):
            if cols[i] & 1:
                ans += m - len-len
        return ans


m, n = 48, 37
indices = [[40, 5]]
a = Solution()
ans = a.oddCells(m, n, indices)
print(ans)
