from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        max_end_time = max(endTime)
        if queryTime > max_end_time:
            return 0
        cnt = [0] * (max_end_time + 2)
        for s, e in zip(startTime, endTime):
            cnt[s] += 1
            cnt[e + 1] -= 1
        return sum(cnt[:queryTime + 1])