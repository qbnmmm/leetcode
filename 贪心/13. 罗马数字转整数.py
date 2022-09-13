class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            if i < n - 1 and s[i:i + 2] in dic.keys():
                ans += dic[s[i: i + 2]]
                i += 2
            else:
                ans += dic[s[i]]
                i += 1
        return ans
