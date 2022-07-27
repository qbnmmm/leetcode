def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    start, end, multi, ans = 0, 0, 1, 0

    while end < len(nums):
        multi *= nums[end]
        while multi >= k:
            multi //= nums[start]
            start += 1

        ans += end - start + 1
        end += 1
    return ans


nums = [10, 5, 2, 6]
l = 100
print(numSubarrayProductLessThanK(nums, l))
