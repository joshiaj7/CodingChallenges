"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)

        ordered = sorted(heights)

        for i in range(n):
            if ordered[i] != heights[i]:
                ans += 1

        return ans
