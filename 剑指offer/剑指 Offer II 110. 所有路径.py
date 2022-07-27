class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        ans = []
        def dfs(node: int, path: list[int]):
            if node == n - 1:
                ans.append(path[:])
                return
            next = graph[node]
            for nextNode in next:
                path.append(nextNode)
                dfs(nextNode, path)
                path.pop()
            return
        dfs(0, [0])
        return ans