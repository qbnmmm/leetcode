class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        l, r = 0, 1
        tmp = set()
        tmp.add(s[0])
        ans = 1
        while r < n:
            while s[r] in tmp:
                tmp.remove(s[l])
                l += 1
            tmp.add(s[r])
            r += 1
            ans = max(ans, len(tmp))
        return ans

a = Solution()
s = "abcabcbb"
ans = a.lengthOfLongestSubstring(s)