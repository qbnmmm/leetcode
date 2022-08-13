class Solution:
    def reverseWords(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 先反转每个单词，再反转整个数组
        cur = 0
        n = len(s)
        while cur < n:
            l = r = cur
            while r < n and s[r] != " ":
                r += 1
            cur = r + 1
            r -= 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1