class Solution:
    def gcd(self, a: int, b: int) -> int:
        if b > a:
            a, b = b, a
        while a % b:
            mod = a % b
            a, b = b, mod
        return b

    def fractionAddition(self, expression: str) -> str:
        denominator, numerator = 0, 1  # 分子分母
        i, n = 0, len(expression)
        while i < n:
            denominator1, sign = 0, 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1
            denominator1 = sign * denominator1
            i += 1

            # 读取分母
            numerator1 = 0
            while i < n and expression[i].isdigit():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1
            denominator = denominator * numerator1 + denominator1 * numerator
            numerator *= numerator1
        if denominator == 0:
            return "0/1"
        g = self.gcd(abs(denominator), numerator)
        return f"{denominator // g}/{numerator // g}"
