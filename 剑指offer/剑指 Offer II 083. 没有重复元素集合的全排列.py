class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backTrack(nums: list[int])->None:
            if not nums:
                ans.append(path[:])
                return
            for num in nums:
                tmp = nums[:]
                tmp.remove(num)
                path.append(num)
                backTrack(tmp)
                path.pop()
        ans = []
        path = []
        backTrack(nums)
        return ans