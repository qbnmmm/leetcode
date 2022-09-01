import collections
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 单调栈，带下标
        n = len(prices)
        q = collections.deque()
        ans = [-1] * n
        for i in range(n):
            if not q or q[-1][0] < prices[i]:
                q.append((prices[i], i))
            else:
                while q and q[-1][0] >= prices[i]:
                    val, idx = q.pop()
                    ans[idx] = val - prices[i]
                q.append((prices[i], i))
        while q:
            val, idx = q.pop()
            ans[idx] = val
        return ans