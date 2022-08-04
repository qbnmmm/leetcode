class Trie:

    def __init__(self):
        self.isEnd = False
        self.childs = [None] * 26


    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.childs[idx]:
                cur.childs[idx] = Trie()
            cur = cur.childs[idx]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.childs[idx]:
                return False
            cur = cur.childs[idx]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.childs[idx]:
                return False
            cur = cur.childs[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)