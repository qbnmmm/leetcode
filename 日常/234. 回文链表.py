# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slow, fast = head, head
        while fast.next and fast.next.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            stack.append(slow.val)
        slow = slow.next
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True