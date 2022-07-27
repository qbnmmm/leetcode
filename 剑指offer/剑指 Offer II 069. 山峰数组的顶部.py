class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return left