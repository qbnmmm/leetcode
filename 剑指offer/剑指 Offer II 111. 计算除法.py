import collections


class Solution:
    def dfs(self, graph: collections.defaultdict, x: str, target: str, temp: int, visited: dict) -> int:
        if x == target:
            return temp
        for next_item in graph[x]:
            next_node, weight = next_item
            if not visited[next_node]:
                visited[next_node] = True
                res = self.dfs(graph, next_node, target, temp * weight, visited)
                visited[next_node] = False
                if res != -1:  # 找到答案了直接返回，否则继续DFS
                    return res
        return -1

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = collections.defaultdict(list)
        node = set()  # 统计结点
        for i, (x, y) in enumerate(equations):  # 构建图
            graph[x].append((y, values[i]))
            graph[y].append((x, 1 / values[i]))
            node.add(x)
            node.add(y)
        res = []
        visited = {x: False for x in node}  # 访问过的结点，避免死循环
        # 求解
        for x, y in queries:
            if (x not in node) or (y not in node):  # 结点没出现过，返回-1
                res.append(-1)
                continue
            visited[x] = True
            ans = self.dfs(graph, x, y, 1, visited)  # DFS返回答案
            visited[x] = False
            res.append(ans)
        return res


a = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
ans = a.calcEquation(equations=equations, values=values, queries=queries)
print(ans)
