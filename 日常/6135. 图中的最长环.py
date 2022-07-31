class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        time = [0] * n
        clock = 1
        ans = -1

        for i in range(n):
            if time[i]: # 访问过该结点
                continue
            start_time = clock
            x = i
            while x != -1:
                if time[x]: # 访问过该结点
                    '''
                    这里遇到了访问过的结点有两种情况，一是遇到了环，二是遇到之前找环时遍历过的点；
                    其区别就是时间，如果该结点的时间戳大于等于开始时间（该结点遍历时间晚于本次遍历开始时间）
                    即找到了环
                    '''
                    if time[x] >= start_time:
                        ans = max(ans, clock - time[x])
                    break
                time[x] = clock
                clock += 1
                x = edges[x]
        return ans