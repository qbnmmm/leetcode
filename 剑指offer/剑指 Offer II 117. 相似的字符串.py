import collections


class Solution:
    def __init__(self):
        self.ID = 0
        self.dic = {}

    def getID(self, word: str):
        self.dic[self.ID] = word
        self.ID += 1

    def similar(self, wordA: str, wordB: str) -> bool:
        diff = 0
        for i in range(len(wordA)):
            if wordA[i] != wordB[i]:
                diff += 1
        return diff == 2 or diff == 0

    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        graph = [[0] * n for _ in range(n)]
        for word in strs:
            self.getID(word)
        # 邻接矩阵
        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][i] = 1
                    continue
                if self.similar(self.dic[i], self.dic[j]):
                    graph[i][j] = 1
        vis = [False for _ in range(n)]
        ans = 0

        def dfs(i: int):
            vis[i] = True
            neighbors = graph[i]
            for nb in range(n):
                if nb != i and neighbors[nb] == 1 and not vis[nb]:
                    dfs(nb)
        # 遍历
        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)

        return ans

strs = ["tars","rats","arts","star"]
a = Solution()
ans = a.numSimilarGroups(strs)
print(ans)