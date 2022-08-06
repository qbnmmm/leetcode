# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # 特殊情况处理
        if depth == 1:
            dummy = TreeNode(val)
            dummy.left = root
            return dummy

        q = collections.deque([root])
        tmp = collections.deque()
        d = 1
        while q:
            # 遍历当前层内结点
            cur = q.popleft()
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)

            # 如果是插入前的一层：
            if d == depth - 1:

                l = cur.left
                cur.left = TreeNode(val)
                cur.left.left = l

                r = cur.right
                cur.right = TreeNode(val)
                cur.right.right = r

            # 当前层遍历完毕
            if not q:
                tmp, q = q, tmp
                d += 1
        return root