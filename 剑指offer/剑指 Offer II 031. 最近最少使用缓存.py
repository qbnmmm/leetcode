class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToHead(self, node: DLinkNode):
        head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head
        head.prev = node

    def removeNode(self, node: DLinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node: DLinkNode):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self) -> DLinkNode:
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkNode(key=key, value=value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.removeTail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
