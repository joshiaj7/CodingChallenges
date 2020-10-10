"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0

        if len(points) == 0:
            return 0

        points.sort(key=lambda a: a[1])

        cur = -1
        for s, e in points:
            if cur == -1:
                cur = e
                ans += 1
                continue

            if cur < s:
                cur = e
                ans += 1

        return ans
