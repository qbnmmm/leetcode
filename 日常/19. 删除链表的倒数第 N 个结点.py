# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans, front = head, head
        for _ in range(n):
            front = front.next
        if not front: # 因为下面的判断成立的前提是front指针不为空，当front为空时，说明删除的元素就是第一个
            return head.next
        while front.next:
            ans = ans.next
            front = front.next
        ans.next = ans.next.next
        return head