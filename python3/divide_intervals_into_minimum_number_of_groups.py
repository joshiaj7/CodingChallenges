from typing import List

"""
Space   : O(m)
Time    : O(n log n)
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted([x[0] for x in intervals])
        end_times = sorted([x[1] for x in intervals])
        end_ptr, groups = 0, 0

        for start in start_times:
            if start > end_times[end_ptr]:
                end_ptr += 1
            else:
                groups += 1

        return groups
        