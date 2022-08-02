class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        if k != 0:
            head = ListNode()
            cur = head
            for i in range(k - 1):
                newNode = ListNode()
                cur.next = newNode
                cur = cur.next
            cur.next = head
            self.head = head
            self.tail = head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.isEmpty():
            self.tail = self.tail.next
        self.tail.val = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.val = -1
        if self.size != 1:
            self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.head.val

    def Rear(self) -> int:
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()