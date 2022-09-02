# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left1 = left + 1 if root.left and root.left.val == root.val else 0
            right1 = right + 1 if root.right and root.right.val == root.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)
        dfs(root)
        return ans