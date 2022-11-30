from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        nset = set(nums)
        while head:
            if head.val in nset:
                while head and head.val in nset:
                    head = head.next
                ans += 1
            else:
                head = head.next
        return ans