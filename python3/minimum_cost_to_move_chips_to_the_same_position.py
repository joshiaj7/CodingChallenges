"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n = len(position)

        if n == 0:
            return 0

        odd, even = 0, 0

        for i in position:
            if i % 2 == 1:
                odd += 1
            else:
                even += 1

        return min(odd, even)
