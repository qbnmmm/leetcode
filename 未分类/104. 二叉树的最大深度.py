# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = collections.deque([root])
        tmp = collections.deque()
        while q:
            cur = q.popleft()
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
            if not q:
                ans += 1
                q, tmp = tmp, q
        return ans