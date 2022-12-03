class Solution:
    def secondHighest(self, s: str) -> int:
        n = len(s)
        first, second = -1, -1
        for i in range(n):
            if s[i].isdigit():
                tmp = int(s[i])
                if tmp > first:
                    first, second = tmp, first
                elif first > tmp > second:
                    second = tmp
                else:
                    continue
        if second != -1:
            return second
        else:
            return -1