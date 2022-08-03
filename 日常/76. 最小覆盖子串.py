from collections import defaultdict, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def isEmpty(dic: defaultdict[int]) -> bool:
            for v in dic.values():
                if v > 0:
                    return False
            return True

        n = len(s)
        if n < len(t):
            return ""
        dic = defaultdict(int)
        vis = set()
        for c in t:
            dic[c] += 1
            vis.add(c)

        q = deque()
        ans = []
        for r in range(n):
            if s[r] in vis:
                dic[s[r]] -= 1
            q.append(s[r])

            while isEmpty(dic):
                if not ans:
                    ans = list(q)
                if len(ans) > len(q):
                    ans = list(q)
                tmp = q.popleft()
                if tmp in vis:
                    dic[tmp] += 1
        return ''.join(ans)

a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
ans = a.minWindow(s, t)
print(ans)