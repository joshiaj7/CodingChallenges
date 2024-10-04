from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        n = len(skill)

        if n == 2:
            return skill[0] * skill[1]
        
        skill.sort()

        s = 0
        for i in range(n//2):
            first = skill[i]
            last = skill[n-i-1]

            if s == 0:
                s = first + last
            elif s != first + last:
                return -1

            ans += first * last

        return ans
        