class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        cnt = 0
        set1, set2 = set(), set()
        for i in range(n):
            if s1[i] != s2[i]:
                cnt += 1
                set1.add(s1[i])
                set2.add(s2[i])
        return (cnt == 0 or cnt == 2) and set1 == set2
