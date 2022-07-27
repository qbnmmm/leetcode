class Trie:
    def __init__(self):
        self.childs = [None for _ in range(26)]
        self.isEnd = False


class Solution:
    def findPrefix(self, node: Trie, prefix: str) -> str:
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - ord('a')
            if node.childs[idx]:
                if node.childs[idx].isEnd:
                    return prefix[:i + 1]
            else:
                return prefix
            node = node.childs[idx]
        return prefix

    def insert(self, node: Trie, word: str) -> None:
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if not node.childs[idx]:
                node.childs[idx] = Trie()
            node = node.childs[idx]
        node.isEnd = True

    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            self.insert(root, word)
        sentenceSplit = str.split(sentence, ' ')
        for i in range(len(sentenceSplit)):
            sentenceSplit[i] = self.findPrefix(root, sentenceSplit[i])
        return ' '.join(sentenceSplit)
