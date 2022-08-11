# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        # 复制结点插入到原结点的后面
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        cur = head
        # 复制结点的随机指针
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 拆分链表
        cur = ans = head.next
        pre = head
        while cur.next:
            pre.next = cur.next
            pre = pre.next
            cur.next = pre.next
            cur = cur.next
        pre.next = None
        return ans