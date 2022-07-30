# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        heap = []
        for l in lists:
            head = l
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        dummy = ListNode()
        cur = dummy
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return dummy.next