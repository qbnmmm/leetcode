class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        # 特殊情况处理：nums为空，讨论lower和upper的关系
        if not nums:
            if lower != upper:
                return [str(lower) + "->" + str(upper)]
            else:
                return [str(lower)]
        n = len(nums)
        res = []

        if nums[0] != lower:
            res.append((lower, nums[0] - 1))
        for i in range(n - 1):
            if nums[i + 1] - nums[i] > 1:
                res.append((nums[i] + 1, nums[i + 1] - 1))
        if upper != nums[n - 1]:
            res.append((nums[n - 1] + 1, upper))

        ans = []
        for i in res:
            if i[0] == i[1]:
                ans.append(str(i[0]))
            else:
                ans.append(str(i[0]) + "->" + str(i[1]))
        return ans