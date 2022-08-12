# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        dummy = TreeNode()
        def dfs(root: Optional[TreeNode]):
            if not root.left and not root.right:
                dummy.left = root
                return
            # 因为题目规定有左结点就有右结点，所以不需要讨论只有单个子结点的情况
            dfs(root.left)
            root.left.left = root.right
            root.left.right = root
            root.right = None
            root.left = None
        dfs(root)
        return dummy.left
