from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for i in range(n):
            left = 0
            left_num = 0
            tmp = 0
            while left < i:
                if boxes[left] == '1':
                    left_num += 1
                tmp += left_num
                left += 1
            right = n - 1
            right_num = 0
            while right > i:
                if boxes[right] == '1':
                    right_num += 1
                tmp += right_num
                right -= 1
            ans.append(tmp)
        return ans