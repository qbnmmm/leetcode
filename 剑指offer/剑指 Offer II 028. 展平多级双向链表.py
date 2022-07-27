class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            cur = node
            last = None
            while cur:
                next = cur.next
                if cur.child:
                    childLast = dfs(cur.child)
                    cur.next = cur.child
                    cur.child.prev = cur
                    if next:
                        childLast.next = next
                        next.prev = childLast
                    cur.child = None
                    last = childLast
                else:
                    last = cur
                cur = next
            return last

        dfs(head)
        return head
