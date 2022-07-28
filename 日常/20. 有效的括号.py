class Solution:
    def __init__(self):
        self.stack = []

    def isValid(self, s: str) -> bool:
        hashMap = {'}': '{', ')': '(', ']': '['}
        for ch in s:
            if ch in ['{', '(', '[']:
                self.stack.append(ch)
            else:
                if not self.stack:
                    return False
                if self.stack[-1] == hashMap[ch]:
                    self.stack.pop()
                else:
                    return False
        return not self.stack