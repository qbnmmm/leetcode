class ListNode:
    def __init__(self, val=0, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class MyCircularDeque:

    # 最好不要用list
    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = ListNode(pre=self.head)
        self.head.next = self.tail
        self.capacity = k
        self.size = 0

    def insertHead(self, val: int):
        nxt = self.head.next
        self.head.next = ListNode(val=val)
        self.head.next.next = nxt
        nxt.pre = self.head.next
        self.head.next.pre = self.head

    def insertTail(self, val: int):
        pr = self.tail.pre
        self.tail.pre = ListNode(val=val)
        self.tail.pre.pre = pr
        pr.next = self.tail.pre
        self.tail.pre.next = self.tail

    def delHead(self):
        nxt = self.head.next.next
        self.head.next.next = None
        self.head.next.pre = None
        self.head.next = nxt
        nxt.pre = self.head

    def delTail(self):
        pr = self.tail.pre.pre
        self.tail.pre.pre = None
        self.tail.pre.next = None
        self.tail.pre = pr
        pr.next = self.tail

    def insertFront(self, value: int) -> bool:
        if self.size < self.capacity:
            self.insertHead(value)
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.capacity:
            self.insertTail(value)
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.delHead()
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.delTail()
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        return -1 if not self.size else self.head.next.val

    def getRear(self) -> int:
        return -1 if not self.size else self.tail.pre.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
