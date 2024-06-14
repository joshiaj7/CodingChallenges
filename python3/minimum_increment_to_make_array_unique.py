from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        tracker = 0
        minIncrement = 0

        for x in nums:
            tracker = max(x, tracker)
            minIncrement += tracker - x
            tracker += 1

        return minIncrement
