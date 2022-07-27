class Trie:
    def __init__(self, val=0):
        self.childs = [None for _ in range(26)]
        self.Val = val


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        if key in self.dic:
            tmp = self.dic[key]
            self.dic[key] = val
            val -= tmp
        else:
            self.dic[key] = val
        for i in range(len(key)):
            idx = ord(key[i]) - ord('a')
            if node.childs[idx] is None:
                node.childs[idx] = Trie(val)
            else:
                node.childs[idx].Val += val
            node = node.childs[idx]

    def sum(self, prefix: str) -> int:
        node = self.root
        ans = 0
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - ord('a')
            if node.childs[idx] is None:
                return 0
            node = node.childs[idx]
            ans = node.Val
        return ans

a = MapSum()
apple = "apple"
a.insert(apple,3)
print(a.sum("ap"))
a.insert("app",2)
print(a.sum("ap"))
a.insert(apple,5)
a.insert(apple,1)
print(a.sum("apple"))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
