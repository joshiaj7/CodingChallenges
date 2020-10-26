"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ev, od = [], []

        for x in A:
            if x % 2 == 0:
                ev.append(x)
            else:
                od.append(x)

        return sorted(ev) + sorted(od)
