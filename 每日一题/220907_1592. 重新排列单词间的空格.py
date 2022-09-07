class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = 0
        n = len(text)
        tmp = ''
        words = []
        for i in range(n):
            if text[i] == ' ':
                if tmp:
                    words.append(tmp)
                    tmp = ''
                space += 1
            else:
                tmp += text[i]
        if tmp:
            words.append(tmp)
        word_num = len(words)

        if word_num == 1:  # 特殊情况处理
            ans = words[0]
            for _ in range(space):
                ans += ' '
            return ans

        last = space % (word_num - 1)
        mid = space // (word_num - 1)
        tmp = ''
        for _ in range(mid):
            tmp += ' '
        ans = ""
        for i in range(word_num - 1):
            ans += words[i] + tmp
        ans += words[-1]
        for _ in range(last):
            ans += ' '
        return ans


a = Solution()
s = " practice   makes   perfect"
anss = a.reorderSpaces(s)
print(anss)
