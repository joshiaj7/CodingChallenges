"""
Space   : O(1)
Time    : O(log N)
"""


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = (minutesToTest // minutesToDie) + 1

        x = 0
        while t**x < buckets:
            x += 1

        return x
