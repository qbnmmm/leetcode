class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans, path = [], []
        n = len(s)

        def backTrack(l: int) -> None:
            if len(path) > 4: #长度超过四个了，剪枝
                return
            if l == n and len(path) == 4:
                ans.append('.'.join(path))
                return
            for i in range(l + 1, min(l + 4, n + 1)):
                cur = s[l:i]
                if (len(cur) > 1 and cur[0] == '0') or int(cur) > 255: #前缀0和大于255的都丢弃
                    continue
                path.append(cur[:])
                backTrack(i)
                path.pop()
        backTrack(0)
        return ans