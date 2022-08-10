class Solution:
    def __calc(self, s: str) -> list[int]:
        ans = [0, 0]  # 常数, x的系数
        pos = True
        n = len(s)
        tmp = "0"
        for i in range(n):
            if s[i] == '+' or s[i] == '-':
                ans[0] += int(tmp) if pos else -int(tmp)
                tmp = "0"
                if s[i] == '-':
                    pos = False
                else:
                    pos = True
            elif s[i] == 'x':
                if tmp == "0":
                    ans[1] += 1 if pos else -1
                else:
                    ans[1] += int(tmp) if pos else -int(tmp)
                tmp = "0"
            else:
                tmp += s[i]
        if tmp:
            ans[0] += int(tmp) if pos else -int(tmp)
        return ans

    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        l = self.__calc(left)
        r = self.__calc(right)
        x_num = l[1] - r[1]
        const = r[0] - l[0]
        if x_num == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        ans = const // x_num
        return "x=" + str(ans)


s = "-x=-1"
a = Solution()
ans = a.solveEquation(s)
print(ans)
