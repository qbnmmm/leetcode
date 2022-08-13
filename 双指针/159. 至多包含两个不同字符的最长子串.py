import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        # 用队列代替双指针更易于理解
        q = collections.deque()
        dic = collections.defaultdict(int)
        vis = set()
        ans = 0
        for c in s:
            q.append(c)
            vis.add(c)
            if len(vis) == 3:
                while True:
                    cur = q.popleft()
                    dic[cur] -= 1
                    if not dic[cur]:
                        vis.remove(cur)
                        break
            dic[c] += 1
            ans = max(ans, len(q))
        return ans