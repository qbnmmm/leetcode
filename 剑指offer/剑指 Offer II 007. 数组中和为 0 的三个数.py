def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    ans = list()
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:  # 为了和上一次枚举的数不同
            continue
        target = -nums[first]
        third = n - 1
        for second in range(first + 1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:  # 为了和上一次枚举的数不同
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])
    return ans
