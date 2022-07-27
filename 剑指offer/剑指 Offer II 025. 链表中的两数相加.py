class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    carry = 0
    ans = None
    while s1 or s2 or carry != 0:
        a = 0 if not s1 else s1.pop()
        b = 0 if not s2 else s2.pop()
        res = a + b + carry
        cur = res % 10
        carry = res // 10
        curNode = ListNode(cur, ans)
        ans = curNode
    return ans
