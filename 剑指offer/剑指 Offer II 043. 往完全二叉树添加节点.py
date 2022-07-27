class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = [self.root]
        i = 0
        while i < len(self.queue):
            if self.queue[i].left:
                self.queue.append(self.queue[i].left)
            if self.queue[i].right:
                self.queue.append(self.queue[i].right)
            i += 1

    def insert(self, v: int) -> int:
        node = TreeNode(val=v)
        idx = len(self.queue)
        father = self.queue[int((idx-1)/2)]
        if idx % 2 == 1:
            father.left = node
        else:
            father.right = node
        self.queue.append(node)
        return father.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()