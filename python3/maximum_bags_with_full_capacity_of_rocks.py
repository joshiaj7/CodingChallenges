"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        ans = 0
        disc = []

        for i in range(n):
            if capacity[i] - rocks[i] == 0:
                ans += 1
            else:
                disc.append(capacity[i] - rocks[i])

        disc.sort()
        while disc and additionalRocks > 0:
            req = disc.pop(0)
            if additionalRocks - req < 0:
                return ans
            additionalRocks -= req
            ans += 1

        return ans
