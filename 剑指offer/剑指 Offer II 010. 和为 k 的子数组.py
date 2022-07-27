def subarraySum(nums: list[int], k: int) -> int:
    ret = pre_sum = 0
    pre_dict = {0: 1}
    for i in nums:
        pre_sum += i
        ret += pre_dict.get(pre_sum - k, 0)
        pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1
    return ret


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))
