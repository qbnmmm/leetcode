class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():  # 3.6以后dic本就是有序的
            if v:
                return k
        return ' '
