def countBits(n: int) -> list[int]:
    ans = [0]
    if n == 0:
        return ans
    jishu = True
    for i in range(1, n+1):
        if jishu:
            ans.append(ans[i-1]+1)
        else:
            ans.append(ans[i//2])
        jishu = not jishu
    return ans

print(countBits(10))
