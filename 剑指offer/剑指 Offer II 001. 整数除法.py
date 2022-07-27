def divide(a: int, b: int) -> int:
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
    if a == INT_MIN and b == -1:
        return INT_MAX
    ans = 0

    # 处理边界，防止转正数溢出
    if b == INT_MIN:  # 除数绝对值最大，结果必为0或1
        return 1 if a == b else 0
    if a == INT_MIN:  # 被除数先减去一个除数
        a -= -abs(b)
        ans += 1

    sign = -1 if (a > 0) ^ (b > 0) else 1

    a, b = abs(a), abs(b)
    for i in range(31, -1, -1):  # [31,0]
        if (a >> i) - b >= 0:
            a = a - (b << i)
            if ans > INT_MAX - (1 << i):  # ans >= INT_MAX时（这里不解）
                return INT_MIN
            ans += 1 << i
    return ans if sign == 1 else -ans
