import collections
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:(mp[x], -x)) if (mp := collections.Counter(nums)) else nums


a = Solution()
nums = [1, 1, 2, 2, 2, 3]
ans = a.frequencySort(nums)
print(ans)
