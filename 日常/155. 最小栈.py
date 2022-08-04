class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.miniStack or val <= self.miniStack[-1]:
            self.miniStack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.miniStack[-1]:
            self.miniStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miniStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()