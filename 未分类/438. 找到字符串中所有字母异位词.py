import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        m, n = len(s), len(p)
        if m < n:
            return ans

        cnt = collections.Counter(p)
        need = n

        for right in range(m):

            ch = s[right]
            if ch in cnt:
                cnt[ch] -= 1
                if cnt[ch] >= 0:
                    need -= 1

            left = right - n
            if left >= 0:
                ch = s[left]
                if ch in cnt:
                    cnt[ch] += 1
                    if cnt[ch] > 0:
                        need += 1

            if need == 0:
                ans.append(right - n + 1)
        return ans


s = "abacbabc"
p = "abc"
a = Solution()
ans = a.findAnagrams(s, p)
print(ans)
