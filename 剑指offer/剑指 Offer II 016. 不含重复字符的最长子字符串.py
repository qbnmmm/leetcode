def lengthOfLongestSubstring(s: str) -> int:
    hashMap = {}
    ans = left = res = 0
    lens = len(s)
    for right in range(lens):
        loc = hashMap.get(s[right], -1)
        if loc < left:
            hashMap[s[right]] = right
            res += 1
        else:
            ans = max(ans, res)
            left = hashMap[s[right]] + 1
            hashMap[s[right]] = right
            res = right - left + 1
    ans = max(ans, res)
    return ans