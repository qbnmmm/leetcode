class Solution:
    def read(self, number: str) -> str:
        ans = ""
        for c in number:
            if c.isdigit():
                ans += c
        return ans

    def reformat(self, number: str) -> str:
        n = len(number)
        i = 0
        ans = ""
        while n - i > 4:
            ans += number[i:i + 3] + '-'
            i += 3
        if n - i == 4:
            ans += number[i:i + 2] + '-' + number[i + 2:]
        else:
            ans += number[i:]
        return ans

    def reformatNumber(self, number: str) -> str:
        number = self.read(number)
        return self.reformat(number)