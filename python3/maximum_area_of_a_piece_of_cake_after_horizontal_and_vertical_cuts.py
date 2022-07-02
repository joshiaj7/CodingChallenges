"""
Space : O(n)
Time  : O(n log n)
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hc = [0] + sorted(horizontalCuts) + [h]
        vc = [0] + sorted(verticalCuts) + [w]
        mh = mv = 0

        for i in range(1, len(hc)):
            mh = max(mh, hc[i] - hc[i-1])

        for i in range(1, len(vc)):
            mv = max(mv, vc[i] - vc[i-1])

        return (mh * mv) % (10**9 + 7)
