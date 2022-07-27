import bisect


class MyCalendar:

    def __init__(self):
        self.starts, self.ends = [], []

    def book(self, start: int, end: int) -> bool:
        if not self.starts:
            self.starts.append(start)
            self.ends.append(end)
            return True
        pos = bisect.bisect_left(self.starts, start)
        if pos == 0 and end <= self.starts[0]:
            self.starts.insert(0, start)
            self.ends.insert(0, end)
            return True
        elif pos == 0 or start < self.ends[pos - 1]:
            return False
        elif pos == len(self.starts) or end <= self.starts[pos]:
            self.starts.insert(pos, start)
            self.ends.insert(pos, end)
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
