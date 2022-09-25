from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        ans = []
        for i in range(n):
            tmp = 0
            step = 1
            if k < 0:
                step = -1
            for j in range(step, k + step, step):
                tmp += code[(i + j) % n]
            ans.append(tmp)
        return ans