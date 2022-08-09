class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = (len(nums1) + len(nums2) - 1) // 2
        y = (len(nums1) + len(nums2)) // 2
        i, j, med = 0, 0, 0
        while i + j <= y:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    mid = nums1[i]
                    i += 1
                else:
                    mid = nums2[j]
                    j += 1
            elif i < len(nums1):
                mid = nums1[i]
                i += 1
            elif j < len(nums2):
                mid = nums2[j]
                j += 1

            if i + j > x:
                med += mid

        if x != y:
            med /= 2
        return med