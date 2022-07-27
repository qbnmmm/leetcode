class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # 如果两个都是叶子直接或运算返回
        if quadTree1.isLeaf and quadTree2.isLeaf:
            quadTree1.val = quadTree1.val | quadTree2.val
            return quadTree1
        # 其中之一为叶子则看条件直接返回
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            return quadTree1
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        # 都是叶子且值相同
        if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
            return Node(topRight.val, 1, None, None, None, None)
        # 返回新构造的值
        return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight)
