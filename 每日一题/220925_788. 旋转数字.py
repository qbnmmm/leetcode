class Solution:
    def isLegal(self, n: int) -> bool:
        num = str(n)
        if '3' in num or '4' in num or '7' in num:
            return False
        if '2' in num or '5' in num or '6' in num or '9' in num:
            return True
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if self.isLegal(i):
                ans += 1
        return ans