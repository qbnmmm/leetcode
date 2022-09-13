class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        sig = 1
        ans = 0
        state = 0
        '''
        状态：0:开始时的空格 1: 符号 2: 数字前导0 3: 数字 4: 数字后的字符 5: 非法
        其实状态0
        结束状态3、4
        状态转移：
        0 -> 0 空格
        0 -> 1 +-
        0 -> 2 0
        0 -> 3 1-9
        0 -> 4 .以及a-z
        1 -> 2 0
        1 -> 3 1-9
        1 -> 5 其他
        2 -> 2 0
        2 -> 3 1-9
        2 -> 4 其他
        3 -> 3 0-9
        3 -> 4 其他
        '''
        for c in s:
            if state == 0:
                if c == ' ':
                    continue
                elif c == '+' or c == '-':
                    state = 1
                    if c == '-':
                        sig = -1
                elif c == '0':
                    state = 2
                elif c.isdigit():
                    ans *= 10
                    ans += int(c)
                    state = 3
                else:
                    return 0
            elif state == 1:
                if c == '0':
                    state = 2
                elif c.isdigit():
                    ans *= 10
                    ans += int(c)
                    state = 3
                else:
                    return 0
            elif state == 2:
                if c == '0':
                    continue
                elif c.isdigit():
                    ans *= 10
                    ans += int(c)
                    state = 3
                else:
                    return 0
            else:
                if c.isdigit():
                    ans *= 10
                    ans += int(c)
                else:
                    break
        ans *= sig
        if ans > MAX:
            return MAX
        if ans < MIN:
            return MIN
        return ans