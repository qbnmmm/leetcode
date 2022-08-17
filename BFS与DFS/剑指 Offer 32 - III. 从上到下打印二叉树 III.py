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
        reverse = False
        q = collections.deque([root])
        tmp = collections.deque()
        while q:
            cur = q.pop()
            res.append(cur.val)
            if reverse:
                if cur.right: tmp.append(cur.right)
                if cur.left: tmp.append(cur.left)
            else:
                if cur.left: tmp.append(cur.left)
                if cur.right: tmp.append(cur.right)
            if not q:
                ans.append(res[:])
                res = []
                q, tmp = tmp, q
                reverse = not reverse
        return ans