def validPalindrome(s: str) -> bool:
    def isLegal(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    n = len(s)
    if n <= 1:
        return True
    left, right = 0, n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return isLegal(s, left + 1, right) or isLegal(s, left, right - 1)
    return True
