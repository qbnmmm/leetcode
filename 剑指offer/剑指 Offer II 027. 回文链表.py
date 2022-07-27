class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head,head
        stack = []
        while fast.next != None and fast.next.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast.next != None and fast.next.next == None:
            stack.append(slow.val)
        slow = slow.next
        while slow != None:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True