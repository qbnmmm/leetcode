# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        n = 0
        dummy = ListNode(next=head)
        cur = head
        while cur:
            cur = cur.next
            n += 1
        len = 1
        while len < n:
            beforeHead = dummy
            while beforeHead:
                mid = beforeHead.next
                for _ in range(len):
                    if mid:
                        mid = mid.next
                    else:
                        break
                afterTail = mid
                for _ in range(len):
                    if afterTail:
                        afterTail = afterTail.next
                    else:
                        break
                self.Merge(beforeHead, mid, afterTail)
                for _ in range(len * 2):
                    if beforeHead:
                        beforeHead = beforeHead.next
                    else:
                        break
            len *= 2
        return dummy.next

    def Merge(self, beforeHead: ListNode, mid: ListNode, afterTail: ListNode):
        cur = beforeHead
        head1 = cur.next
        head2 = mid
        while head1 != mid and head2 != afterTail:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        while head1 != mid:
            cur.next = head1
            head1 = head1.next
            cur = cur.next
        while head2 != afterTail:
            cur.next = head2
            head2 = head2.next
            cur = cur.next
        cur.next = afterTail

head = ListNode(4, next=ListNode(2, next=ListNode(1, next=ListNode(3))))
a = Solution()
ans = a.sortList(head)
print(ans)
