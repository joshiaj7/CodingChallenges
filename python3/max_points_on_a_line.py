from collections import defaultdict
from math import inf

"""
Space   : O(n)
Time    : O(n^2)
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 1

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1 - x2 == 0:
                return inf
            return (y1 - y2) / (x1 - x2)

        for i in range(n):
            slopes = defaultdict(int)
            for j in range(i+1, n):
                slope = find_slope(points[i], points[j])
                slopes[slope] += 1
                ans = max(slopes[slope], ans)

        return ans + 1
