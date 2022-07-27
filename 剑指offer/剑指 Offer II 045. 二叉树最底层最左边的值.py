# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        ans = root
        while queue:
            q = queue
            queue = []
            ans = q[0]
            for i in q:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
        return ans.val