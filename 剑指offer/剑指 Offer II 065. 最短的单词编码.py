class Trie:
    def __init__(self, depth=1):
        self.childs = [None for _ in range(26)]
        self.depth = depth
        self.isStart = False


class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        def isEnd(node: Trie) -> bool:
            for i in range(26):
                if node.childs[i]:
                    return False
            return True
        words = list(set(words))
        root = Trie()
        ans = 0
        for word in words:
            node = root
            for i in range(len(word) - 1, -1, -1):
                idx = ord(word[i]) - ord('a')
                if node.childs[idx] is None:
                    node.childs[idx] = Trie(node.depth + 1)
                node = node.childs[idx]
                if node.isStart:
                    ans -= node.depth
                    node.isStart = False
            if isEnd(node):
                ans += node.depth
                node.isStart = True
        return ans


words = ["atime","time","btime"]
a = Solution()
ans = a.minimumLengthEncoding(words)
print(ans)
