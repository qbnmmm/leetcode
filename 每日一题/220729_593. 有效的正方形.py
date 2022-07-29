class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        points = [p1, p2, p3, p4]
        distance = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if j != i:
                    distance[i][j] = (abs(points[i][0] - points[j][0])) ** 2 + (abs(points[i][1] - points[j][1])) ** 2
        for i in range(4):
            tmp = sorted(distance[i])
            if tmp[1] == tmp[2] and tmp[1] + tmp[2] == tmp[3]:
                continue
            else:
                return False
        return True