class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        if len(timePoints) > 1440: return 0
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        mins.append(mins[0] + 1440)
        return min(mins[i] - mins[i-1] for i in range(1, len(mins)))
