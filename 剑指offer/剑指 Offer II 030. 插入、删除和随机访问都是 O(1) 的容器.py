class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict: return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict: return False
        index = self.dict.get(val)
        self.list[index], self.list[-1] = self.list[-1], self.list[index]
        self.dict[self.list[index]] = index
        del self.dict[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
