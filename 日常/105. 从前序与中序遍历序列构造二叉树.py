# Definition for a binary tree node.
import bisect
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        loc = inorder.index(root.val)
        left_pre = preorder[1: loc + 1]
        if loc < n:
            right_pre = preorder[loc + 1:]
        else:
            right_pre = []
        left_in = inorder[:loc]
        if loc < n:
            right_in = inorder[loc + 1:]
        else:
            right_in = []
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root