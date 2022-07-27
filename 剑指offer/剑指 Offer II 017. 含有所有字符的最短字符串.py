def minWindow(s: str, t: str) -> str:
    ls, lt = len(s), len(t)
    if ls < lt:
        return ''
    import collections
    cnt = collections.Counter(t)
    need = lt
    start, end = 0, -1
    min_len = ls + 1
    left = 0
    for right in range(ls):
        ch = s[right]
        if ch in cnt:
            if cnt[ch] > 0:
                need -= 1
            cnt[ch] -= 1

        while need == 0:
            str_len = right - left + 1
            if str_len < min_len:
                min_len = str_len
                start, end = left, right
            ch = s[left]
            if ch in cnt:
                if cnt[ch] >= 0:
                    need += 1
                cnt[ch] += 1
            left += 1
    return s[start: end + 1]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
