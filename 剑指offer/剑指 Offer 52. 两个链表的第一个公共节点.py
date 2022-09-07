# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB
        while l1 != l2:
            if not l1:
                l1 = headB
                l2 = l2.next
            elif not l2:
                l2 = headA
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        return l1
