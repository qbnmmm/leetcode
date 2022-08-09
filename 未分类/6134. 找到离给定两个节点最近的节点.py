from math import inf


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)
        ans = -1
        min_dis = inf

        def calc_dis(x: int) -> list[int]:
            dis = [inf] * n
            d = 0
            while x != -1 and dis[x] == inf:
                dis[x] = d
                d += 1
                x = edges[x]
            return dis

        for i, d1, d2 in zip(range(n), calc_dis(node1), calc_dis(node2)):
            d = max(d1, d2)
            if d < min_dis:
                min_dis = d
                ans = i

        return ans