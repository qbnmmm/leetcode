from itertools import accumulate  # 累加
from string import ascii_lowercase
from typing import List

c2i = {c: i for i, c in enumerate(ascii_lowercase)}

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for start, end, dir in shifts:
            diff[start] += dir * 2 - 1
            diff[end] -= dir * 2 - 1
        ans = ''.join(ascii_lowercase[(c2i[c] + shift) % 26] for c, shift in zip(s, accumulate(diff)))
        return ans