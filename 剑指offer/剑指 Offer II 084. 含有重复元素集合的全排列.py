class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backTrack():
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not vis[i - 1]:
                    continue
                if not vis[i]:
                    vis[i] = True
                    path.append(nums[i])
                    backTrack()
                    vis[i] = False
                    path.pop()

        ans, path = [], []
        nums.sort()
        n = len(nums)
        vis = [False] * n
        backTrack()
        return ans

nums = [1,1,2]
a = Solution()
ans = a.permuteUnique(nums)
print(ans)