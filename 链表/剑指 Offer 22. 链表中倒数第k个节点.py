# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        r = head
        l = head
        for _ in range(k):
            r = r.next
        while r:
            l = l.next
            r = r.next
        return l
