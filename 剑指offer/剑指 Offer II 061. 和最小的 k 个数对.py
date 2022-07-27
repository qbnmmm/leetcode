import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        a, b = len(nums1), len(nums2)
        k = min(k, a * b)
        a, b = min(a, k), min(b, k)
        minHeap = []
        for i in range(a):
            for j in range(b):
                tmp = nums1[i] + nums2[j]
                heapq.heappush(minHeap, (-tmp, nums1[i], nums2[j]))
                while len(minHeap) > k:
                    heapq.heappop(minHeap)
        ans = []
        while minHeap:
            res = heapq.heappop(minHeap)
            ans.append([res[1], res[2]])
        return ans


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
a = Solution()
ans = a.kSmallestPairs(nums1, nums2, k)
print(ans)