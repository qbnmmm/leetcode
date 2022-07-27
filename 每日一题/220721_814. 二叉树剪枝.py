# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if node.left:
                if not dfs(node.left):
                    node.left = None
            if node.right:
                if not dfs(node.right):
                    node.right = None
            if not (node.left or node.right) and node.val == 0:
                return False
            return True

        if not dfs(root):
            return None
        return root