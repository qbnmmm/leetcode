# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root: TreeNode, curr: int) -> int:
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)


def newnode(val: int) -> TreeNode:
    return TreeNode(val=val)


root = newnode(10)
root.left = newnode(5)
root.right = newnode(-3)
root.left.left = newnode(3)
root.left.right = newnode(2)
root.right.right = newnode(11)
root.left.left.left = newnode(3)
root.left.left.right = newnode(-2)
root.left.right.right = newnode(1)
target = 8
a = Solution()
ans = a.pathSum(root, target)
print(ans)
