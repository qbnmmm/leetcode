# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def __init__(self):
        self.ans = 0
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        map = {}

        def dfs(root: TreeNode, u: int, depth: int):
            """
            :param root: 根节点
            :param u: 编号
            :param depth: 深度
            """
            if not root:
                return
            if depth not in map.keys():
                map[depth] = u
            self.ans = max(self.ans, u - map[depth] + 1)
            u -= map[depth] + 1
            dfs(root.left, u << 1, depth + 1)  # 左子树编号
            dfs(root.right, u << 1 | 1, depth + 1)  # 右子树编号

        dfs(root, 1, 0)
        return self.ans