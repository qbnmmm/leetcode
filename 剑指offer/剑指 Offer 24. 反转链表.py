# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []

        def dfs(node: ListNode):
            if not node:
                return
            stack.append(node)
            dfs(node.next)

        dummy = ListNode(0)
        dfs(head)
        cur = dummy
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return dummy.next