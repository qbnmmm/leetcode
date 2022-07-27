def singleNumber(nums: list[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones = (num ^ ones) & ~twos
        twos = (num ^ twos) & ~ones
    return ones

nums = [2,2,3,2,5,5,6,5,6,6]
ans = singleNumber(nums)
print(ans)
