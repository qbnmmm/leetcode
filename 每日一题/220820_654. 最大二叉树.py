# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def buildTree(l, r):
            if l > r:
                return None
            rootIndex = nums.index(max(nums[l:r + 1]))
            root = TreeNode(nums[rootIndex])
            root.left = buildTree(l, rootIndex - 1)
            root.right = buildTree(rootIndex + 1, r)
            return root

        ans = buildTree(0, n - 1)
        return ans