class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans, counter = 0, 0
        for num in nums:
            if counter == 0:
                ans = num
                counter = 1
            else:
                if num == ans:
                    counter += 1
                else:
                    counter -= 1
        return ans