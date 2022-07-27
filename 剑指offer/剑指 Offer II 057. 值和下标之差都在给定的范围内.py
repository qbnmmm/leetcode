class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        def getID(x: int, w: int) -> int:
            if x >= 0:
                return x // w
            return (x + 1) // w - 1

        mp = {}
        for idx, num in enumerate(nums):
            id = getID(num, t + 1)
            if id in mp:
                return True
            elif id - 1 in mp and abs(num - mp[id - 1]) <= t:
                return True
            elif id + 1 in mp and abs(num - mp[id + 1]) <= t:
                return True
            mp[id] = num
            if idx - k >= 0:
                del mp[getID(nums[idx - k], t + 1)]
        return False
