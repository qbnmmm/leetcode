class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        minDiff = 1000000
        arr.sort()
        ans = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < minDiff:
                minDiff = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == minDiff:
                ans.append([arr[i - 1], arr[i]])
        return ans