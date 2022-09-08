from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        odd = k + 1
        even = 1
        ans = []
        for i in range(k + 1):
            if i & 1:
                ans.append(odd)
                odd -= 1
            else:
                ans.append(even)
                even += 1
        for i in range(k + 2, n + 1):
            ans.append(i)
        return ans
