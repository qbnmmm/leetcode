class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def get_score(word: str):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        def dfs(i: int, cur_score: int, cur_letters: List[int]):
            nonlocal ans
            ans = max(ans, cur_score)
            if i == len(words):
                return
            for j in range(i, len(words)):
                new_letters = [cur_letters[k] - words[j].count(chr(k + ord('a'))) for k in range(26)]
                if any(x < 0 for x in new_letters):
                    continue
                dfs(j + 1, cur_score + get_score(words[j]), new_letters)

        ans = 0
        dfs(0, 0, [letters.count(chr(i + ord('a'))) for i in range(26)])
        return ans
        