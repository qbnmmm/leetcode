from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        node_in, node_out = defaultdict(set), defaultdict(set)
        for link in prerequisites:
            node_in[link[0]].add(link[1])
            node_out[link[1]].add(link[0])
        q = deque()
        ans = 0
        for i in range(numCourses):
            if not node_in[i]:
                q.append(i)
        while q:
            cur = q.popleft()
            ans += 1
            nxt = node_out[cur]
            for node in nxt:
                node_in[node].remove(cur)
                if not node_in[node]:
                    q.append(node)
        return ans == numCourses