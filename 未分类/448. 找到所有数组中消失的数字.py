class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        newNums = nums[:]
        for i in range(n):
            newNums[nums[i] - 1] += n
        ans = []
        for i in range(n):
            if newNums[i] <= n:
                ans.append(i + 1)
        return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
a = Solution()
ans = a.findDisappearedNumbers(nums)
print(ans)