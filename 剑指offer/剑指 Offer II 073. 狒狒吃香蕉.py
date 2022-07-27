import math


class Solution:
    def calTime(self, piles: list[int], k):
        ans = 0
        for pile in piles:
            ans += math.ceil(pile / k)
        return ans

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r, ans = 1, max(piles), -1
        while l <= r:
            mid = (l + r) >> 1
            if self.calTime(piles, mid) > h:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans
