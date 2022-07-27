def findAnagrams(self, s: str, p: str) -> list[int]:
    lens, lenp = len(s), len(p)
    ans, cnt = [], [0 for _ in range(26)]
    if lens < lenp: return ans
    for i in range(lenp):
        cnt[ord(p[i]) - ord('a')] -= 1
        cnt[ord(s[i]) - ord('a')] += 1
    diff = 0
    for num in cnt:
        if num != 0:
            diff += 1
    if diff == 0:
        ans.append(0)
    for i in range(lenp, lens):
        x, y = s[i], s[i - lenp]  # x进y出
        if cnt[ord(x) - ord('a')] == 0:
            diff += 1
        cnt[ord(x) - ord('a')] += 1
        if cnt[ord(x) - ord('a')] == 0:
            diff -= 1
        if cnt[ord(y) - ord('a')] == 0:
            diff += 1
        cnt[ord(y) - ord('a')] -= 1
        if cnt[ord(y) - ord('a')] == 0:
            diff -= 1
        if diff == 0:
            ans.append(i - lenp + 1)
    return ans
