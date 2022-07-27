class RecentCounter:

    def __init__(self):
        self.queue = []
        self.timelimit = 3000

    def ping(self, t: int) -> int:
        i = 0
        self.queue.append(t)
        while self.queue[i] + self.timelimit < t:
            i += 1
        self.queue = self.queue[i:]
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)