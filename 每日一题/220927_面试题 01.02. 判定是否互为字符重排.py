import collections


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return s1 != s2 and collections.Counter(s1) == collections.Counter(s2)