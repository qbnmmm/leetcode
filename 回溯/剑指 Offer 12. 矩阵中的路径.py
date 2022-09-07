from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def traceback(idx: int, vis: set, i: int, j: int) -> bool:
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 \
                    or (i, j) in vis or word[idx] != board[i][j]:
                return False
            if idx == len(word) - 1:
                return True
            ans = False
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                vis.add((i, j))
                ans = ans or traceback(idx + 1, vis, i + di, j + dj)
                vis.remove((i, j))
            return ans

        for i in range(m):
            for j in range(n):
                if traceback(0, set(), i, j):
                    return True
        return False