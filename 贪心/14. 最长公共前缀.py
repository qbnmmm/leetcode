from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        n = len(strs)
        if n == 1:
            return ans
        for i in range(1, n):
            for j in range(len(ans)):
                if j < len(strs[i]) and strs[i][j] == ans[j]:
                    continue
                else:
                    ans = ans[:j]
                    break
            if not ans:
                return ans
        return ans


strs = ["flower", "flow", "flight"]
a = Solution()
ans = a.longestCommonPrefix(strs)
print(ans)
