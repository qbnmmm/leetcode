from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.capacity = n
        self.q = ['#'] * n
        self.ptr = 0


    def insert(self, idKey: int, value: str) -> List[str]:
        self.q[idKey - 1] = value
        ans = []
        while self.ptr < self.capacity and self.q[self.ptr] != '#':
            ans.append(self.q[self.ptr])
            self.ptr += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)