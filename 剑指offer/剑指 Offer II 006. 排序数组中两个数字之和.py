def twoSum(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        while numbers[i] + numbers[j] > target:
            j -= 1
        if numbers[i] + numbers[j] == target:
            return [i, j]
        i += 1
    return [i, j]
