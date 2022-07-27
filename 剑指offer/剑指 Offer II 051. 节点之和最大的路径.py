# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(root: TreeNode) -> int:
            if not root:
                return 0
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)

            priceNewPath = root.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, priceNewPath)
            return root.val + max(leftGain, rightGain)
        maxGain(root)
        return self.maxSum