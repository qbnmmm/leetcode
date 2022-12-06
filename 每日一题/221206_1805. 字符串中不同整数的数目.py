class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        tmp = ''
        for c in word:
            if c.isdigit():
                tmp += c
            else:
                if tmp:
                    s.add(int(tmp))
                    tmp = ''
        if tmp:
            s.add(int(tmp))
        return len(s)
