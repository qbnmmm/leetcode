import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        dic = collections.defaultdict(set)
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                dic[cur.val].add(cur.left.val)
                dic[cur.left.val].add(cur.val)
            if cur.right:
                q.append(cur.right)
                dic[cur.val].add(cur.right.val)
                dic[cur.right.val].add(cur.val)
        n = len(dic)
        vis = set()
        if len(vis) == n:
            return 0
        qq = collections.deque([start])
        tmp = collections.deque()
        flag = False
        ans = 0
        while qq:
            cur = qq.popleft()
            vis.add(cur)
            for node in dic[cur]:
                if node not in vis:
                    flag = True
                    tmp.append(node)
            if not qq:
                if flag:
                    ans += 1
                    tmp, qq = qq, tmp
                    flag = False
                else:
                    break
        return ans