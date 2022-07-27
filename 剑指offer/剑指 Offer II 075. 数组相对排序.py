class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        hashMap = [0 for _ in range(1001)]
        ans = []
        for i in arr1:
            hashMap[i] += 1
        for num in arr2:
            while hashMap[num] > 0:
                ans.append(num)
                hashMap[num] -= 1
        for idx, val in enumerate(hashMap):
            while val != 0:
                ans.append(idx)
                val -= 1
        return ans