import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        length = len(tasks)
        if length < 2:
            return length
        task_num = collections.Counter(tasks)
        task_sort = sorted(task_num.items(), key=lambda x: x[1], reverse=True)
        max_task_count = task_sort[0][1]
        ans = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                ans += 1

        return max(ans, length)