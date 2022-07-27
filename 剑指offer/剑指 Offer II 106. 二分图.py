class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        UNCOLOERD, RED, GREEN = 0, 1, 2
        colors = [0 for _ in range(n)]
        def dfs(i: int, color: int) -> bool:
            if colors[i] != UNCOLOERD and colors[i] != color:
                return False
            if colors[i] == color:
                return True
            if colors[i] == UNCOLOERD:
                colors[i] = color
                newcolor = RED if color == GREEN else GREEN
                ans = True
                for v in graph[i]:
                    ans &= dfs(v,newcolor)
                return ans
        ans = True
        for i in range(n):
            if colors[i] == UNCOLOERD:
                ans &= dfs(i, RED)
        return ans

graph = [[1,3],[0,2],[1,3],[0,2]]
a = Solution()
ans = a.isBipartite(graph)
print(ans)