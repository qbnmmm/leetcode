# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = []
        self.point = -1
        self.dfs(root)

    def dfs(self, node: TreeNode):
        if not node:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)
        return

    def next(self) -> int:
        self.point += 1
        return self.res[self.point]
    def hasNext(self) -> bool:
        return self.point + 1 < len(self.res)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()