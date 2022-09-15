from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        l = head
        r = head.next
        while l and r:
            nxt = r.next
            pre.next = r
            r.next = l
            l.next = nxt
            pre = l
            l = nxt
            if not l:
                return dummy.next
            r = l.next
        return dummy.next