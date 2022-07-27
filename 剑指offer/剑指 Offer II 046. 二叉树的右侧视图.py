# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            q = queue
            queue = []
            ans.append(q[-1].val)
            for i in q:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
        return ans