# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo, idx, ans = dict(), 0, []

        def dfs(node):
            left = right = None
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            cur = (node.val, left, right)
            if cur in memo:
                if not memo[cur][1]:
                    ans.append(node)
                    memo[cur][1] += 1
                return memo[cur][0]
            else:
                nonlocal idx
                memo[cur] = [idx, 0]
                idx += 1
                return idx - 1

        dfs(root)
        return ans