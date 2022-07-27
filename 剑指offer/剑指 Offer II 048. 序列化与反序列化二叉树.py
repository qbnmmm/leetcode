# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        root.left = self.serialize(root.left)
        root.right = self.serialize(root.right)
        return f"{root.val},{root.left},{root.right}"
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(',')
        def build(queue):
            val = queue.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = build(queue)
            root.right = build(queue)
            return root
        return build(queue)



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# res = deser.deserialize(ser.serialize(root))

tree = [1,2,3,null,null,4,5]