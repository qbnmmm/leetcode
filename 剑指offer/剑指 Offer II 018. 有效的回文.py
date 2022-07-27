def isPalindrome(s: str) -> bool:
    n = len(s)
    if n <= 1:
        return True
    s = s.lower()
    left, right = 0, n - 1
    while left < right:
        if not (s[left].isdigit() or s[left].isalpha()):
            left += 1
            continue
        if not (s[right].isdigit() or s[right].isalpha()):
            right -= 1
            continue
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


s = "A man, a plan, a canal: Panama"
