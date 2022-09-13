class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        dic = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        while num > 0:
            cur = 0
            for k, v in dic.items():
                if num >= k:
                    cur = k
                else:
                    break
            ans += dic[cur]
            num -= cur
        return ans