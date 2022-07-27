import collections


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = collections.defaultdict(int)
        self.wordSet = []

    def getNeighbor(self, word) -> list[str]:
        wordList = list(word)
        ans = []
        for i in range(len(word)):
            tmp = wordList[i]
            wordList[i] = '*'
            neighbor = ''.join(wordList)
            ans.append(neighbor)
            wordList[i] = tmp
        return ans

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            self.wordSet.append(word)
            neighbors = self.getNeighbor(word)
            for neighbor in neighbors:
                self.hashMap[neighbor] += 1
        return

    def search(self, searchWord: str) -> bool:
        neighbors = self.getNeighbor(searchWord)
        for neighbor in neighbors:
            wordfreq = self.hashMap[neighbor]
            if wordfreq > 1:
                return True
            elif wordfreq == 1:
                if searchWord in self.wordSet:
                    continue
                return True
        return False