class WordFilter:

    def __init__(self, words: list[str]):
        self.map = {}
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                for k in range(1, len(word) + 1):
                    self.map[(word[:j], word[-k:])] = i

    def f(self, pref: str, suff: str) -> int:
        return self.map.get((pref, suff), -1)

wordList = ["apple"]
a = WordFilter(wordList)
ans = a.f("a","e")
print(ans)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
