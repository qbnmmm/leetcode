from typing import List

import numpy


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        s = n // 20
        return float(numpy.mean(arr[s: -s]))