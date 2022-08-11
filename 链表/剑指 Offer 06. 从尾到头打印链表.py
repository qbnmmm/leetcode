# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        ans = []

        def dfs(node: ListNode):
            if not node:
                return
            dfs(node.next)
            ans.append(node.val)

        dfs(head)
        return ans