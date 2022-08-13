class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        stack = []
        for num in arr:
            if not stack or stack[-1] <= num:
                stack.append(num)
            elif stack[-1] > num:
                cur = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(cur)
        return len(stack)