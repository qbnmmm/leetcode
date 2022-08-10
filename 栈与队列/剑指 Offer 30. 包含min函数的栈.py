class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ministack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.ministack or x <= self.ministack[-1]:
            self.ministack.append(x)


    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.ministack[-1]:
            self.ministack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.ministack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()