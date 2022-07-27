def minSubArrayLen(target: int, nums: list[int]) -> int:
    head, tail = 0, 0
    n = len(nums)
    res = 0
    ans = n + 1
    while tail < n:
        res += nums[tail]
        while res >= target:
            ans = min(ans, tail - head + 1)
            res -= nums[head]
            head += 1
        tail += 1
    return 0 if ans == n + 1 else ans

target = 15
nums = [1,2,3,4,5]
a = minSubArrayLen(target,nums)
print(a)