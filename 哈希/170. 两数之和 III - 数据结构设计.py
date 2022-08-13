import collections


class TwoSum:

    def __init__(self):
        self.dic = collections.defaultdict(int)
        self.vis = set()

    def add(self, number: int) -> None:
        self.dic[number] += 1
        self.vis.add(number)


    def find(self, value: int) -> bool:
        # 偶数特殊情况
        if not value & 1:
            if self.dic[value // 2] > 1:
                return True
        half = value / 2
        for num in self.vis:
            if num >= half:
                continue
            target = value - num
            if target in self.vis:
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)