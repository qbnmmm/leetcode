import bisect


class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        if self.starts == []:
            self.starts.append(start)
            self.ends.append(end)
            return True
        s = bisect.bisect_left(self.starts, start)
        if s == 0 and end <= self.starts[0]:
            self.starts.insert(s, start)
            self.ends.insert(s, end)
            return True
        elif start < self.ends[s - 1]:
            return False
        elif s == len(self.starts) or end <= self.starts[s]:
            self.starts.insert(s, start)
            self.ends.insert(s, end)
            return True
        else:
            return False


a = MyCalendar()
a.book(47, 50)
a.book(33, 41)
a.book(39, 45)
a.book(33, 42)
a.book(25, 32)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
