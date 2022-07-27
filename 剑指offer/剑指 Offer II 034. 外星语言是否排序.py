class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        def isLegal(word1, word2) -> bool:
            l1, l2 = len(word1), len(word2)
            for i in range(min(l1, l2)):
                first1 = dic[ord(word1[i]) - ord('a')]
                first2 = dic[ord(word2[i]) - ord('a')]
                if first1 > first2:
                    return False
                elif first1 < first2:
                    return True
            if l1 > l2:
                return False
            return True

        dic = [0 for _ in range(26)]
        for i in range(26):
            dic[ord(order[i]) - ord('a')] = i
        for i in range(1, len(words)):
            if not isLegal(words[i - 1], words[i]):
                return False
        return True


a = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
b = a.isAlienSorted(words, order)
print(b)
