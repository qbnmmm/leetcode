class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        n = len(distance)
        forward, back = 0, 0
        flag = False
        for i in range(n):
            cur = (start + i) % n
            if cur == destination:
                flag = True
            if flag:
                forward += distance[cur]
            else:
                back += distance[cur]
        return min(forward, back)