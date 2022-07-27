# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        def mergeTwoList(A: ListNode, B: ListNode) -> ListNode:
            dummy = ListNode()
            cur = dummy
            while A and B:
                if A.val < B.val:
                    cur.next = A
                    A = A.next
                else:
                    cur.next = B
                    B = B.next
                cur = cur.next
            if A:
                cur.next = A
            else:
                cur.next = B
            return dummy.next

        def merge(lists: list[ListNode], l: int, r: int) -> ListNode:
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = (l + r) >> 1
            return mergeTwoList(merge(lists, l, mid), merge(lists, mid + 1, r))

        return merge(lists, 0, len(lists) - 1)


a = ListNode(1, next=ListNode(4, next=ListNode(5)))
b = ListNode(1, next=ListNode(3, next=ListNode(4)))
c = ListNode(1, next=ListNode(3))
lists = [a, b, c]
an = Solution()
ans = an.mergeKLists(lists)
print(ans)
