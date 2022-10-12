class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                cur = stack.pop()
                stack.append(stack.pop() + max(cur * 2, 1))
        return stack[-1]
