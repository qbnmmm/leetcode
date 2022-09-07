# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ans = []

        def traceback(node: TreeNode, tgt: int, path: List[int]):
            if not node.left and not node.right:
                if node.val == tgt:
                    path.append(node.val)
                    ans.append(path[:])
                    path.pop()
                return

            path.append(node.val)
            if node.left:
                traceback(node.left, tgt - node.val, path)
            if node.right:
                traceback(node.right, tgt - node.val, path)
            path.pop()

        if root:
            traceback(root, target, [])
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
a = Solution()
aa = a.pathSum(root, 3)
print(aa)
