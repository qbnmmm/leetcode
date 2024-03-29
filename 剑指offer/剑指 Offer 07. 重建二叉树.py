# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root: int, left: int, right: int):
            if left > right: return
            node = TreeNode(preorder[root])
            i = dic[node.val]
            node.left = recur(root + 1, left, i - 1)
            node.right = recur(i - left + root + 1, i + 1, right)
            return node


        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)
