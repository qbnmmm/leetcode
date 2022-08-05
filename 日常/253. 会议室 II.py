class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = []
        for t in intervals:
            if not rooms:
                rooms.append(t[1])
            else:
                tmp = {}
                for i in range(len(rooms)):
                    if rooms[i] <= t[0]:
                        tmp[rooms[i]] = i
                if not tmp:
                    rooms.append(t[1])
                else:
                    rooms[tmp[max(tmp.keys())]] = t[1]
        return len(rooms)


intervals = [[1293, 2986], [848, 3846], [4284, 5907], [4466, 4781], [518, 2918], [300, 5870]]
a = Solution()
ans = a.minMeetingRooms(intervals)
print(ans)
