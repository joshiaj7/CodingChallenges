from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[1])

        end = float('-inf')
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                ans += 1

        return ans
