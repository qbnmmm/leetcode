def checkInclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False
    cnt = [0 for _ in range(26)]
    for i in range(n):
        cnt[ord(s1[i]) - ord('a')] -= 1
        cnt[ord(s2[i]) - ord('a')] += 1
    diff = 0
    for num in cnt:
        if num != 0:
            diff += 1
    if diff == 0:
        return True
    for i in range(n, m):
        x, y = ord(s2[i]) - ord('a'), ord(s2[i - n]) - ord('a')  # x为进入字符，y为出字符
        if x == y:
            continue
        if cnt[x] == 0:
            diff += 1
        cnt[x] += 1
        if cnt[x] == 0:
            diff -= 1
        if cnt[y] == 0:
            diff += 1
        cnt[y] -= 1
        if cnt[y] == 0:
            diff -= 1
        if diff == 0:
            return True
    return False


s1, s2 = "ab", "eidbaooo"
print(checkInclusion(s1, s2))
