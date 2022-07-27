class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans, pre = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                ans = min(ans + 1, pre)
            else:
                pre += 1
        return ans

s = "0101100011"
a = Solution()
ans = a.minFlipsMonoIncr(s)
print(ans)