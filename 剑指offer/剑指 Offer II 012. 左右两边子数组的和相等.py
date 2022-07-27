def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    res, n = 0, len(nums)
    for i in range(len(nums)):
        if res*2 + nums[i] == total:
            return i
        res += nums[i]
    return -1