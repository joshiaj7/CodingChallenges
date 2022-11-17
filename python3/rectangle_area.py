"""
Space   : O(1)
Time    : O(1)
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1 = (ay2 - ay1) * (ax2 - ax1)
        rec2 = (by2 - by1) * (bx2 - bx1)
        slic = max(min(ay2,by2) - max(ay1,by1), 0) * max(min(ax2,bx2) - max(ax1,bx1), 0)

        return rec1 + rec2 - slic