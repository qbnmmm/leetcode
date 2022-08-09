class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x: int, y: int, cur: int) -> bool:
            if board[x][y] != word[cur]:
                return False
            if cur == len(word) - 1:
                return True
            board[x][y] = '#'

            for choice in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = choice[0] + x, choice[1] + y
                if 0 <= nx < m and 0 <= ny < n and dfs(nx, ny, cur + 1):
                    return True
            board[x][y] = word[cur]

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False