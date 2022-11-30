from collections import Counter


class FreqStack:

    def __init__(self):
        self.cnt = Counter()
        self.stacks = []

    def push(self, val: int) -> None:
        if self.cnt[val] == len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.cnt[val]].append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        self.cnt[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
