class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def dfs(idx: int) -> tuple[int, str]:
            res, multi = "", 0
            while idx < n:
                if s[idx].isdigit():
                    multi = multi * 10 + int(s[idx])
                elif s[idx] == '[':
                    idx, tmp = dfs(idx + 1)
                    res += multi * tmp
                    multi = 0
                elif s[idx] == ']':
                    return idx, res
                else:
                    res += s[idx]
                idx += 1
            return idx, res
        return dfs(0)[1]