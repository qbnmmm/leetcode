class ListNode:
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode(pre=self.head)
        self.head.next = self.tail
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head.next
        while index != 0:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        nxt = self.head.next
        newNode = ListNode(val, self.head, nxt)
        self.head.next = newNode
        nxt.pre = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        pre = self.tail.pre
        newNode = ListNode(val, pre, self.tail)
        pre.next = newNode
        self.tail.pre = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        elif index <= 0:
            self.addAtHead(val)
        else:
            cur = self.head.next
            while index != 0:
                cur = cur.next
                index -= 1
            pre = cur.pre
            newNode = ListNode(val, pre, cur)
            pre.next = newNode
            cur.pre = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.size:
            return
        cur = self.head.next
        while index != 0:
            cur = cur.next
            index -= 1
        pre = cur.pre
        nxt = cur.next
        pre.next = nxt
        nxt.pre = pre
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
