"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        n = len(costs)

        costs.sort()
        i = 0
        while i < n and coins - costs[i] >= 0:
            coins -= costs[i]
            ans += 1
            i += 1

        return ans
