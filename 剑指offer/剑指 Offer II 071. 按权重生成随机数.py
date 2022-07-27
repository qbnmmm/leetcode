import bisect
import random


class Solution:

    def __init__(self, w: list[int]):
        n = len(w)
        self.w = [0] * n
        self.w[0] = w[0]
        for i in range(1, n):
            self.w[i] = self.w[i - 1] + w[i]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, rand)


w = [1, 2, 3, 4]
a = Solution(w)
ans = a.pickIndex()
print(ans)
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()class Solution:
#
#     def __init__(self, w: List[int]):
#
#
#     def pickIndex(self) -> int:
#
#
#
# # Your Solution object will be instantiated and called as such:
# # obj = Solution(w)
# # param_1 = obj.pickIndex()
