class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        dic = {}
        for idx, val in enumerate(arr):
            dic[val] = idx
        dp = [[2] * n for _ in range(n - 1)]
        ret = 0
        for i in range(0, n - 1):
            for j in range(i, n):
                diff = arr[j] - arr[i]
                if diff in dic and dic[diff] < i:
                    idx = dic[diff]
                    dp[i][j] = dp[idx][i] + 1
                    ret = max(ret, dp[i][j])
        return ret
