class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s.replace("()", "")
        return len(s)