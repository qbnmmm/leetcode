def countSubstrings(s: str) -> int:
    def countPalindrome(s: str, left: int, right: int, n: int) -> int:
        res = 0
        while left >= 0 and right < n:
            if s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            else:
                break
        return res

    n = len(s)
    ans = 0
    for i in range(n):
        ans += countPalindrome(s, i, i, n) + countPalindrome(s, i, i + 1, n)
    return ans