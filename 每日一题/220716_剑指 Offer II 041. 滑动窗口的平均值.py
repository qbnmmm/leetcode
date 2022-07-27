class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.capacity = size
        self.size = 0
        self.avg = 0
        self.first = 0

    def next(self, val: int) -> float:
        if self.size < self.capacity:
            self.queue.append(val)
            self.avg = (self.avg * self.size + val) / (self.size + 1)
            self.size += 1
        else:
            out = self.queue[self.first]
            self.queue[self.first] = val
            self.avg += (val-out) / self.capacity
            self.first = (self.first+1) % self.capacity
        return self.avg

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
