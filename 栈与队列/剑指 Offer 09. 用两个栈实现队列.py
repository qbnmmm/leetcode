class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s2.append(value)

    def deleteHead(self) -> int:
        if self.s1:
            return self.s1.pop()
        elif self.s2:
            while self.s2:
                self.s1.append(self.s2.pop())
            return self.s1.pop()
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()