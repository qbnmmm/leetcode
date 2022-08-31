from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        i = j = 0
        while i <= n and j < n:
            if i < n:
                if not stack or stack[-1] != popped[j]:
                    stack.append(pushed[i])
                    i += 1
                else:
                    stack.pop()
                    j += 1
            else:
                if stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    return False
        return True