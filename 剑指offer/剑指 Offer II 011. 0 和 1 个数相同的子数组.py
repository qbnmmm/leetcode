def findMaxLength(nums: list[int]) -> int:
    maxLength, n, counter = 0, len(nums), 0
    mp = {0: -1}
    for i in range(n):
        if nums[i] == 1:
            counter += 1
        else:
            counter -= 1
        if counter in mp.keys():
            maxLength = max(maxLength, i - mp[counter])
        else:
            mp[counter] = i
    return maxLength


nums = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
print(findMaxLength(nums))
