"""
Space   : O(1)
Time    : O(1)
"""


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        x = (minutesToTest // minutesToDie) + 1

        p = 0
        while x**p < buckets:
            p += 1

        return p
