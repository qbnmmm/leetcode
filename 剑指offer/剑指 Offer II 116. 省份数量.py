class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        vis = [False for _ in range(n)]

        def dfs(i: int):
            if vis[i]:
                return
            vis[i] = True
            for j in range(n):
                if j != i and isConnected[i][j] and not vis[j]:
                    dfs(j)

        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)
            else:
                continue
        return ans

isconnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
a = Solution()
ans = a.findCircleNum(isconnected)
print(ans)