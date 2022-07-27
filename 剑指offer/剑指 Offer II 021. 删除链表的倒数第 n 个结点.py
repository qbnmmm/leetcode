class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    front, back = head, head
    for i in range(n):
        front = front.next
    if front == None:
        return head.next
    while front.next != None:
        front = front.next
        back = back.next
    back.next = back.next.next
    return head
