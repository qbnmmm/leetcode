class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def findMidNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def mergeList(self, head1: ListNode, head2: ListNode) -> ListNode:
        l1, l2 = head1, head2
        while l1 and l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l1 = next1
            l2.next = l1
            l2 = next2
        return head1

    def reorderList(self, head: ListNode) -> None:
        mid = self.findMidNode(head)
        tail = self.reverseList(mid)
        self.head = self.mergeList(head, tail)
