"""
Space = O(1)
Time = O(n log n)
"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda a: (a[0], -a[1]))

        end = 0
        for i, j in intervals:
            if j > end:
                ans += 1
            end = max(end, j)

        return ans
