# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSum = 0
        prefixSumTree = {0:1}

        self.dfs(root, targetSum, prefixSum, prefixSumTree)
        return self.count

    def dfs(self, root: TreeNode, sum: int, prefixSum: int, prefixSumTree: dict):
        '''

        :param root: 当前结点
        :param sum: 目标
        :param prefixSum: 前缀和，即从根到当前结点前的所有节点值的和
        :param prefixSumTree: 记录前缀和的字典，键为前缀和，值为个数
        '''
        if not root:
            return 0
        prefixSum += root.val
        oldSum = prefixSum - sum # oldSum表示前缀和与目标sum的距离
        if oldSum in prefixSumTree:
            self.count += prefixSumTree[oldSum]
        prefixSumTree[prefixSum] = prefixSumTree.get(prefixSum, 0) + 1

        self.dfs(root.left, sum, prefixSum, prefixSumTree)
        self.dfs(root.right, sum, prefixSum, prefixSumTree)

        prefixSumTree[prefixSum] -= 1