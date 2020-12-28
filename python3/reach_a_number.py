"""
Space   : O(1)
Time    : O(log n)
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        if target == 0:
            return 0
        if target < 0:
            target = -target
        if target == 1:
            return 1
        step = 1
        farthest = 1
        while farthest < target or farthest % 2 != target % 2:
            step += 1
            farthest += step
        return step
