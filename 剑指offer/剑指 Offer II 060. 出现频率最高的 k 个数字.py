import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numFreq = collections.Counter(nums)
        minHeap = []
        for x, freq in numFreq.items():
            heapq.heappush(minHeap, (freq, x))
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        ans = []
        while minHeap:
            ans.append(heapq.heappop(minHeap)[1])
        return ans
