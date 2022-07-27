def addBinary(a: str, b: str) -> str:
    def add(i=0, j=0, k=0):
        ans = i + j + k
        if ans == 0 or ans == 2:  # 低位
            r1 = 0
        else:
            r1 = 1
        r2 = 1 if ans > 1 else 0  # 进位
        return r1, r2

    l1, l2 = len(a), len(b)
    if l2 > l1:
        l1, l2 = l2, l1  # l1长
        a, b = b, a  # a长

    k = 0  # 进位
    ans = []
    for i in range(-1, -l1 - 1, -1):
        if -i <= l2:
            tmp, k = add(int(a[i]), int(b[i]), k)
            ans.insert(0, str(tmp))
        else:
            tmp, k = add(int(a[i]), k)
            ans.insert(0, str(tmp))
    if k == 1:
        ans.insert(0, '1')
    return ''.join(ans)

a = "11"
b = "1011"
print(addBinary(a,b))
