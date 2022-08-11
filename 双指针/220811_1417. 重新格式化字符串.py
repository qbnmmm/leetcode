class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        digit, char = [], []
        for c in s:
            if c.isdigit():
                digit.append(c)
            else:
                char.append(c)
        if abs(len(digit) - len(char)) > 1:
            return ""
        a = b = 0
        ans = ""
        while a < len(digit) and b < len(char):
            ans += digit[a] + char[b]
            a += 1
            b += 1
        if a < len(digit):
            ans += digit[a]
        if b < len(char):
            ans = char[b] + ans
        return ans
