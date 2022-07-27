# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ans = None
        if p.right:
            ans = p.right
            while ans.left:
                ans = ans.left
            return ans
        node = root
        while node:
            if node.val > p.val:
                ans = node
                node = node.left
            else:
                node = node.right
        return ans