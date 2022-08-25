from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = -1, n
        while l + 1 != r:
            mid = (l + r) >> 1
            if arr[mid] <= x:
                l = mid
            else:
                r = mid
        if l == -1:
            return arr[:k]
        if r == n:
            return arr[n - k:]
        ans = []
        while k:
            if l < 0:
                ans.append(arr[r])
                r += 1
            elif r >= n:
                ans.append(arr[l])
                l -= 1
            else:
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    ans.append(arr[l])
                    l -= 1
                else:
                    ans.append(arr[r])
                    r += 1
            k -= 1
        return sorted(ans)
