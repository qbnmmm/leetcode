class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        i = j = 0
        vis = {s[0]}
        ans = 1
        while j < n - 1:
            j += 1
            while s[j] in vis and i < j:
                vis.remove(s[i])
                i += 1
            if s[j] not in vis:
                vis.add(s[j])
                ans = max(ans, j - i + 1)
        return ans

s = "abcabcbb"
a = Solution()
ans = a.lengthOfLongestSubstring(s)
print(ans)