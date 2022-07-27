import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, -num)
        for i in range(k-1):
            heapq.heappop(res)
        return -heapq.heappop(res)

a = Solution()
res = [3,2,1,5,6,4]
b = a.findKthLargest(res, 2)
print(b)