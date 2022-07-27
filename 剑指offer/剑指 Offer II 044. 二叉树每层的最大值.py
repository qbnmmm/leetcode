# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        ans = []

        def dfs(node: TreeNode, curHeight: int) -> None:
            if not node:
                return
            if curHeight == len(ans):
                ans.append(node.val)
            else:
                ans[curHeight] = max(ans[curHeight], node.val)
            dfs(node.left, curHeight + 1)
            dfs(node.right, curHeight + 1)
        dfs(root, 0)
        return ans
