from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        n = len(energy)
        needEnergy = max(sum(energy) + 1 - initialEnergy, 0)
        maxExperience = max(experience)
        needExperience = 0
        for i in range(n):
            if initialExperience <= experience[i]:
                needExperience += experience[i] - initialExperience + 1
                initialExperience += needExperience
            initialExperience += experience[i]
            if initialExperience > maxExperience:
                break

        ans = needExperience + needEnergy
        return ans
