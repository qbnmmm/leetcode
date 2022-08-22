class Trie:
    def __init__(self):
        self.childs = [None] * 26
        self.num = 1000000


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        strs = sentence.split(' ')
        root = Trie()
        for i in range(len(strs)):
            cur = root
            for c in strs[i]:
                idx = ord(c) - ord('a')
                if not cur.childs[idx]:
                    cur.childs[idx] = Trie()
                cur = cur.childs[idx]
                cur.num = min(cur.num, i + 1)
        find = True
        cur = root
        for c in searchWord:
            idx = ord(c) - ord('a')
            if not cur.childs[idx]:
                find = False
                break
            cur = cur.childs[idx]

        if find:
            return cur.num
        else:
            return -1

a, b = "this problem is an easy problem", "pro"
c = Solution()
ans = c.isPrefixOfWord(a, b)
print(ans)