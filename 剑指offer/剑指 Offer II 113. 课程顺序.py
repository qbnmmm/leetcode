import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph_in = collections.defaultdict(set)
        graph_out = collections.defaultdict(set)
        start = set([i for i in range(numCourses)])
        for y, x in prerequisites:
            graph_in[y].add(x)
            graph_out[x].add(y)
            if y in start:
                start.remove(y)
        q = collections.deque(list(start))
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            for course in graph_out[cur]:
                graph_in[course].remove(cur)
                if not graph_in[course]:
                    q.append(course)
        return ans if len(ans) == numCourses else []

pr = [[0,1],[0,2],[1,2]]
a = Solution()
ans = a.findOrder(3, pr)
print(ans)