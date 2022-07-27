class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def anagrams(s: str) -> list[int]:
            dict = [0 for _ in range(26)]
            for i in s:
                dict[ord(i) - ord('a')] += 1
            return dict
        strMap = {}
        ans = []
        for s in strs:
            dict = anagrams(s)
            hashCode = hash(tuple(dict)) #转成tuple才能哈希
            res = strMap.get(hashCode,[])
            res.append(s)
            strMap[hashCode] = res

        for words in strMap.values():
            ans.append(words)
        return ans

strs = ["eat","tea","tan","ate","nat","bat"]
ans = Solution()
b = ans.groupAnagrams(strs)
print(b)