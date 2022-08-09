import collections


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        g = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            g[a][b] = v
            g[b][a] = 1 / v
        for k in g:
            for i in g:
                for j in g:
                    if k in g[i] and j in g[k]:
                        g[i][j] = g[i][k] * g[k][j]
        ans = []
        for a, b in queries:
            if a in g and b in g[a]:
                ans.append(g[a][b])
            else:
                ans.append(-1.0)
        return ans