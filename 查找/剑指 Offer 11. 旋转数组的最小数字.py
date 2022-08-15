from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if n == 1:
            return numbers[0]

        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:  # 如果左右值相等一定有[i,m]内元素都相等或[m,r]内元素都相等（或两者都满足）。此时没必要二分查找
                return min(numbers[l:r])
        return numbers[l]