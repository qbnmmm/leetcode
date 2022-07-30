# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q, tmp = collections.deque([root]), collections.deque()
        level = 1
        level_res = 0
        ans = 0
        max_value = -1000000
        while q:
            cur = q.popleft()
            level_res += cur.val
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
            if not q:# 一层处理完毕
                if level_res > max_value:
                    ans = level
                    max_value = level_res
                level += 1
                level_res = 0
                if tmp: # 把tmp和q互换，可以理解为把tmp内的元素加入q
                    q, tmp = tmp, q
        return ans