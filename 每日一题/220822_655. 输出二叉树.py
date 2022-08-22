# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def dfs(node: TreeNode) -> int:
            return max(dfs(node.left), dfs(node.right)) + 1 if node else 0

        def dfsTree(node: TreeNode, r: int, c: int):
            ans[r][c] = str(node.val)
            diff = 2 ** (height - 2 - r)
            if node.left:
                dfsTree(node.left, r + 1, c - diff)
            if node.right:
                dfsTree(node.right, r + 1, c + diff)

        height = dfs(root)
        ans = [[""] * (2 ** height - 1) for _ in range(height)]
        dfsTree(root, 0, (len(ans[0]) - 1) // 2)
        return ans
