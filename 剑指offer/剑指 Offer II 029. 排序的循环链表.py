class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        a = Node(val=insertVal)
        if not head:
            a.next = a
            return a
        if head.next == head:
            head.next = a
            a.next = head
            return head
        cur = head
        next = head.next
        while next != head:
            if cur.val <= insertVal <= next.val:
                break
            if cur.val > next.val:
                if insertVal > cur.val or insertVal < next.val:
                    break
            cur = cur.next
            next = next.next
        cur.next = a
        a.next = next
        return head
