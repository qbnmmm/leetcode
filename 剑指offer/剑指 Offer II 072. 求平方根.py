class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) >> 1
            if mid * mid > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans