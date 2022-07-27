class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def cal(a: int, b: int, op: str) -> int:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return int(a / b) #不能用//，因为//是向下取整，负数时有问题

        ops = ['+', '-', '*', '/']
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(cal(int(a), int(b), i))
        return int(stack.pop())


a = Solution()
b = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
ans = a.evalRPN(b)
print(ans)
