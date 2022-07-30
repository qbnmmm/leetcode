# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        head = ListNode()
        node = head
        while cur1 and cur2:
            if cur1.val < cur2.val:
                node.next = cur1
                cur1 = cur1.next
                node = node.next
            else:
                node.next = cur2
                cur2 = cur2.next
                node = node.next
        if cur1:
            node.next = cur1
        if cur2:
            node.next = cur2
        return head.next