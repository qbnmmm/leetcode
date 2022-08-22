import collections


class Solution:
    def largestPalindromic(self, num: str) -> str:
        dic = collections.defaultdict(int)
        for c in num:
            dic[c] += 1
        ans = []
        for i in range(9, -1 ,-1):
            while dic[str(i)] > 1:
                ans.append(i)
                dic[str(i)] -= 2
        while ans and ans[0] == 0:
            ans.pop(0)
        flag = False
        for i in range(9, -1, -1):
            if dic[str(i)]:
                flag = True
                ans.append(i)
                break
        if flag:
            for i in range(len(ans) - 2, -1, -1):
                ans.append(ans[i])
        else:
            for i in range(len(ans) - 1, -1, -1):
                ans.append(ans[i])
        if not ans:
            return '0'
        return ''.join(list(map(str, ans)))