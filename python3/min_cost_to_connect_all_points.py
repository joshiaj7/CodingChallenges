from typing import List

"""
Space : O(n)
Time  : O(n^2)

Method:
Minimum Spanning Tree
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = {(x, y): float('inf') if i else 0 for i,
             (x, y) in enumerate(points)}

        ans = 0
        while d:
            x1, y1 = min(d, key=d.get)
            ans += d.pop((x1, y1))

            for x2, y2 in d:
                d[(x2, y2)] = min(d[(x2, y2)], (abs(x1 - x2) + abs(y1 - y2)))

        return ans
