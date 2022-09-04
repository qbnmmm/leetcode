from math import inf
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans, cur = 0, -inf
        for l, r in pairs:
            if cur < l:
                ans += 1
                cur = r
        return ans