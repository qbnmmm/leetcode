import collections
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return n
        cnt = collections.defaultdict(int)  # 每个数的次数
        freq = collections.defaultdict(int)  # 出现次数为key的数字有value个
        max_freq = 0  # 最大出现次数
        ans = 0

        for i in range(n):
            cnt[nums[i]] += 1
            f = cnt[nums[i]]
            if cnt[nums[i]] > 1:
                freq[f - 1] -= 1
            freq[f] += 1
            if f > max_freq:
                max_freq = f

            '''
            满足答案有三个（并列关系）：
            1.最大出现次数为1
            2.最大出现次数的数字只有一个，其他数字的次数均为最大出现次数减1
            3.只有一个数字出现了一次，其余数字均出现了最大次数
            '''
            condition1 = max_freq == 1
            condition2 = freq[max_freq] == 1 and max_freq + freq[max_freq - 1] * (max_freq - 1) == i + 1
            condition3 = max_freq * freq[max_freq] == i and freq[1] == 1
            if condition1 or condition2 or condition3:
                ans = i + 1
        return ans
