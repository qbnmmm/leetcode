import collections


class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        node_in, node_out = collections.defaultdict(set), collections.defaultdict(set)
        for q in sequences:
            n = len(q)
            for i in range(n):
                if i > 0:
                    node_in[q[i]].add(q[i - 1])
                if i < n - 1:
                    node_out[q[i]].add(q[i + 1])
        Q = collections.deque()
        n = len(nums)
        ans = []
        for i in range(1, n + 1):
            if len(node_in[i]) == 0:
                Q.append(i)
        if len(Q) != 1:
            return False
        while len(Q) == 1:
            cur = Q.popleft()
            ans.append(cur)
            out = node_out[cur]
            for i in out:
                node_in[i].remove(cur)
                if len(node_in[i]) == 0:
                    Q.append(i)
        if len(Q) > 1:
            return False
        else:
            return True if ans == nums else False


seq = [[1, 2], [1, 3], [2, 3]]
nums = [1, 2, 3]
a = Solution()
ans = a.sequenceReconstruction(nums, seq)
print(ans)
