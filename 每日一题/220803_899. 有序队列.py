class Solution:
    def compare(self, l1: list[str], l2: list[str]) -> int:  # 1.l1小，0.相等，-1，l2小
        for i in range(len(l1)):
            if l1[i] < l2[i]:
                return 1
            elif l1[i] > l2[i]:
                return -1
        return 0

    def orderlyQueue(self, s: str, k: int) -> str:
        sList = list(s)
        if k == 1:
            ans = sList[:]
            for _ in range(len(s)):
                sList.append(sList[0])
                sList = sList[1:]
                res = self.compare(sList, ans)
                if res == 0:
                    return ''.join(ans)
                if res == 1:
                    ans = sList[:]
            return ''.join(ans)
        else:
            return ''.join(sorted(sList))


s = "v"
a = Solution()
ans = a.orderlyQueue(s, 1)
print(ans)
