class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: ListNode) -> ListNode:
    fast, slow = head, head
    while True:
        if not (fast and fast.next):
            return None
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    fast = head
    while True:
        if fast == slow:
            break
        fast = fast.next
        slow = slow.next
    return fast