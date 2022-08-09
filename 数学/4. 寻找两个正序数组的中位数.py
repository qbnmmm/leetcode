class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 如果总共有奇数个元素，x和y相等
        x = (len(nums1) + len(nums2) - 1) // 2
        y = (len(nums1) + len(nums2)) // 2
        i, j, med = 0, 0, 0  # i, j分别指向nums1,nums2
        while i + j <= y:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    mid = nums1[i]
                    i += 1
                else:
                    mid = nums2[j]
                    j += 1
            elif i < len(nums1):  # nums2全在前半段
                mid = nums1[i]
                i += 1
            elif j < len(nums2):  # nums1全在前半段
                mid = nums2[j]
                j += 1

            if i + j > x:  # 如果有偶数个元素，med就是两数之和
                med += mid

        if x != y:  # 总共偶数个元素
            med /= 2
        return med
