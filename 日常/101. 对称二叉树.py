# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        qL, qR = collections.deque([root]), collections.deque([root])
        while qL and qR:
            curL, curR = qL.popleft(), qR.popleft()
            if not curL or not curR:
                if curL or curR:
                    return False
                else:
                    continue
            if curL.val != curR.val:
                return False
            if curL.left:
                qL.append(curL.left)
            else:
                qL.append(None)
            if curL.right:
                qL.append(curL.right)
            else:
                qL.append(None)

            if curR.right:
                qR.append(curR.right)
            else:
                qR.append(None)
            if curR.left:
                qR.append(curR.left)
            else:
                qR.append(None)
        return True