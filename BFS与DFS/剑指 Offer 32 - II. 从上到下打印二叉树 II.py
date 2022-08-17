# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        res = []
        q = collections.deque([root])
        tmp = collections.deque()
        while q:
            cur = q.popleft()
            res.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
            if not q:
                ans.append(res[:])
                res = []
                tmp, q = q, tmp
        return ans