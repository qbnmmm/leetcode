class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(S: list[str], left: int, right: int) -> None:
            if len(S) == n * 2:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        ans = []
        backtrack([], 0, 0)
        return ans

a = Solution()
b = a.generateParenthesis(3)
print(b)