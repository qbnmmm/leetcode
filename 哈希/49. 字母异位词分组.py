import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = collections.defaultdict(list)
        ans = []

        def cal_hash(word: str) -> str:
            return ''.join(sorted(list(word)))

        for word in strs:
            dic[cal_hash(word)].append(word)
        for v in dic.values():
            ans.append(v)
        return ans