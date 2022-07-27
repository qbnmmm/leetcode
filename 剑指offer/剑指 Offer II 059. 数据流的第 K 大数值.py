import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.size = k
        for num in nums:
            self._push(num)

    def _push(self, num: int) -> None:
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, num)
        else:
            if self.heap[0] < num:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        self._push(val)
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)