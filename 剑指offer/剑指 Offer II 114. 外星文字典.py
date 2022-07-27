import collections


class Solution:
    def __init__(self):
        """
        :param charList:字符集合，记录所有出现过的字符
        """
        self.charList = set()

    def addWord(self, word: str):
        """
        把所有字符添加到集合中
        :param word:单词
        """
        for i in range(len(word)):
            self.charList.add(word[i])

    def diff(self, A: str, B: str) -> list:
        """
        比较前后单词的第一处不同，如果A是B的一部分则返回[-1,-1]
        :param A: 前面的单词
        :param B: 后面的单词
        :return: 不同之处的两个字符
        """
        n = min(len(A), len(B))
        for i in range(n):
            if A[i] != B[i]:
                return [A[i], B[i]]
        if len(A) > len(B): # B是A从头开始的一部分，而且B的字典序还在A之后，不合法
            return [0, 0]
        return [-1, -1]

    def alienOrder(self, words: list[str]) -> str:
        node_in, node_out = collections.defaultdict(set), collections.defaultdict(set)
        self.addWord(words[0])
        n = len(words)
        if n == 1:  # 只有一个单词，直接返回即可
            return words[0]

        # 计算每个字符的入度和出度
        for i in range(n - 1):
            self.addWord(words[i + 1])
            node1, node2 = self.diff(words[i], words[i + 1])
            if node1 == -1:
                continue
            if node1 == 0:
                return ""
            node_in[node2].add(node1)
            node_out[node1].add(node2)

        # 把每个入度为0的字符加入队列
        q = collections.deque()
        for c in self.charList:
            if not node_in[c]:
                q.append(c)

        # 把队列中的字符依次取出，并把其从后继字符的node_in中去除
        ans = []
        while q:
            cur = q.popleft()
            ans.append(cur)
            after = node_out[cur]
            for c in after:
                node_in[c].remove(cur)
                if not node_in[c]:  # 如果此时c的入度为0,则加入队列
                    q.append(c)

        # 如果图中有环，就会导致环中字符不会出现在ans里，从而ans比字符集合短
        if len(ans) < len(self.charList):
            return ""
        return "".join(ans)


words = ["abc", "ab"]
a = Solution()
ans = a.alienOrder(words)
print(ans)
