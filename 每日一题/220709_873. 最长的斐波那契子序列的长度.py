class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        dic = {}
        for idx, val in enumerate(arr):
            dic[val] = idx
        dp = [[2] * n for _ in range(n - 1)]
        ret = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                diff = arr[j] - arr[i]
                if diff in dic and dic[diff] < i:
                    k = dic[diff]
                    dp[i][j] = dp[k][i] + 1
                    ret = max(ret, dp[i][j])
        return ret


arr = [1, 2, 3, 4, 5, 6, 7, 8]
a = Solution()
ans = a.lenLongestFibSubseq(arr)
print(ans)