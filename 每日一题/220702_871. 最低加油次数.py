import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        '''
        cur:当前油量能达到的最远距离
        q:大顶堆（因为python中的heapq的堆是小顶堆，因此需要用负数存储
        ans:加油次数
        '''
        cur, q, ans = startFuel, [], 0
        for pos, fuel in stations+ [[target, 0]]: #这里加[[target, 0]]是把终点看作最后一个加油站，而且油量为0
            while cur < pos: #加油条件：车的油量不足以到达下个加油站时，需要从大顶堆弹出一个最大油量的加油站进行加油
                if not q: return -1 #堆中无油，代表车辆无法到达下个加油站
                cur += -heapq.heappop(q)
                ans += 1
            heapq.heappush(q, -fuel) #不需要加油，把油量存入堆中
        return ans
