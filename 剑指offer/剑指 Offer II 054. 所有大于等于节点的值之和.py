# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.res = 0
        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.right)
            node.val += self.res
            self.res = node.val
            dfs(node.left)
            return
        dfs(root)
        return root