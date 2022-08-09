# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def robInternal(self, root: TreeNode) -> list[int]:
        '''
        res[0]代表不偷当前结点所能偷到的钱
        res[0]即为两个孩子（不管偷不偷）结点能偷到的钱的总和
        res[1]代表偷当前结点所能偷到的钱
        res[1]即为两个孩子不偷能偷到的钱的和加上自己的钱
        '''
        res = [0, 0]
        if not root:
            return res
        left = self.robInternal(root.left)
        right = self.robInternal(root.right)
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        return res

    def rob(self, root: Optional[TreeNode]) -> int:
        ans = self.robInternal(root)
        return max(ans)