class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_num, y_num = 0, 0
        if s1 == s2:
            return 0
        
        n = len(s1)
        p, q = 0, 0
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x' and s2[i] == 'y':
                p += 1
            if s1[i] == 'y' and s2[i] == 'x':
                q += 1
        
        if (p + q) & 1:
            return -1
        return p // 2 + q // 2 + (p % 2) * 2
        