import collections

class ListNode:
    def __init__(self, key = -1, val=-1):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = collections.defaultdict(ListNode)
        self.capacity = capacity
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        cur = self.head
        pre = self.head
        for _ in range(capacity):
            cur.next = ListNode()
            cur = cur.next
            cur.pre = pre
            pre = cur
        cur.next = self.tail
        self.tail.pre = cur

    def get(self, key: int) -> int:
        node = self.hashMap[key]
        if node.val == -1:
            return -1
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.hashMap[key].val != -1: # key存在，修改value
            self.hashMap[key].val = value
            self.move_to_head(self.hashMap[key])
        else:
            node = self.tail.pre
            if self.size == self.capacity: # 缓存满
                self.hashMap.pop(node.key)
            else:
                self.size += 1
            self.hashMap[key] = node
            node.key = key
            node.val = value
            self.move_to_head(node)

    def move_to_head(self, node: ListNode) ->None:
        # 拿开结点，前后相连
        pre = node.pre
        nxt= node.next
        pre.next = nxt
        nxt.pre = pre

        # 插入头部
        head_next = self.head.next
        self.head.next = node
        node.next = head_next
        head_next.pre = node
        node.pre = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)