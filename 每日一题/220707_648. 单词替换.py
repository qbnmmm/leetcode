class Trie:
    def __init__(self):
        self.childs = [None for _ in range(26)]
        self.isEnd = False


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = Trie()

        for word in dictionary:
            node = root
            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                if node.childs[idx] is None:
                    node.childs[idx] = Trie()
                node = node.childs[idx]
            node.isEnd = True

        ans = []
        for word in sentence.split():
            node = root
            res = word
            i = 0
            while i < len(word):
                idx = ord(word[i]) - ord('a')
                if node.childs[idx] is None:
                    i = -1
                    break
                node = node.childs[idx]
                if node.isEnd:
                    break
                i += 1
            if i == -1:
                ans.append(res)
            else:
                ans.append(res[:i + 1])
        return " ".join(ans)

dic = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
a = Solution()
ans = a.replaceWords(dic, sentence)
print(ans)