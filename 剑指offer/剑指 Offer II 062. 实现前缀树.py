class TrieNode:

    def __init__(self, char=''):
        self.char = char
        self.childs = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in range(len(word)):
            if node.childs.get(word[i], 0) == 0:
                node.childs[word[i]] = TrieNode(word[i])
                node = node.childs[word[i]]
            else:
                node = node.childs[word[i]]
        node.childs[''] = '.'  # 结束符号
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in range(len(word)):
            if node.childs.get(word[i], 0) == 0:
                return False
            else:
                node = node.childs[word[i]]
        if node.childs.get('', 0) == '.':
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in range(len(prefix)):
            if node.childs.get(prefix[i], 0) == 0:
                return False
            else:
                node = node.childs[prefix[i]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
