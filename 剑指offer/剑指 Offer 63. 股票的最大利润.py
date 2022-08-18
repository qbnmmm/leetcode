from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        n = len(prices)
        ans = 0
        for i in range(n):
            min_price = min(min_price, prices[i])
            ans = max(ans, prices[i] - min_price)
        return ans