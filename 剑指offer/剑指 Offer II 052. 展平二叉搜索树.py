# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummyNode = TreeNode()
        self.resNode = dummyNode
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            self.resNode.right = node
            node.left = None
            self.resNode = node
            inorder(node.right)
            return
        inorder(root)
        return dummyNode.right