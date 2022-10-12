import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        factors = [3, 5, 7]
        vis = {1}
        heap = [1]

        for i in range(k - 1):
            cur = heapq.heappop(heap)
            for factor in factors:
                if (nxt := cur * factor) not in vis:
                    vis.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)
