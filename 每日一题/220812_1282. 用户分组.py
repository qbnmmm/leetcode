import collections


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        dic = collections.defaultdict(list)
        ans = []
        for idx, groupsize in enumerate(groupSizes):
            dic[groupsize].append(idx)
            if groupsize == len(dic[groupsize]):  # 满了就加到ans中
                ans.append(dic[groupsize][:])
                dic[groupsize] = []
        return ans