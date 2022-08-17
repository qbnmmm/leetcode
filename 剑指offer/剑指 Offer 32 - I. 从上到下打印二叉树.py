# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        q = collections.deque([root])
        tmp = collections.deque()
        while q:
            cur = q.popleft()
            ans.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
            if not q:
                q, tmp = tmp, q
        return ans