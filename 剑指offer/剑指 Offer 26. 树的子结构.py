# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        q = collections.deque([A])
        while q:
            cur = q.popleft()
            if self.isSameTree(cur, B):
                return True
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return False
