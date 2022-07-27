class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    la, lb = headA, headB
    flagA, flagB = False, False
    while True:
        if la == lb:
            return la
        la = la.next
        lb = lb.next
        if la == None:
            if flagA:
                return None
            flagA = True
            la = headB
        if lb == None:
            if flagB:
                return None
            lb = headA