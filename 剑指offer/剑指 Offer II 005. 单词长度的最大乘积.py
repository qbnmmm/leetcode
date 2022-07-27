def maxProduct(self, words: list[str]) -> int:
    n = len(words)
    masks = [0 for _ in range(n)]
    for i in range(n):
        for j in range(len(words[i])):
            masks[i] |= 1 << (ord(words[i][j]) - ord('a'))
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans
