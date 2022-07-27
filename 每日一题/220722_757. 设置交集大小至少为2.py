class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        temp = [-1, -1]
        for x in intervals:
            if x[0] <= temp[-2]:
                continue

            if x[0] > temp[-1]:
                temp.append(x[-1] - 1)
            temp.append(x[1])
        return len(temp) - 2

intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
a = Solution()
ans = a.intersectionSizeTwo(intervals)
print(ans)