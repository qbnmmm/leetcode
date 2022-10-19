import collections
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        n = len(sandwiches)
        i = 0
        cnt = 0
        while i != n and cnt != len(students):
            if students[0] == sandwiches[i]:
                students.popleft()
                i += 1
                cnt = 0
            else:
                students.append(students.popleft())
                cnt += 1
        return len(students)