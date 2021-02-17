"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        a, b = 0, len(height) - 1

        while a < b:
            ans = max(ans, (b - a) * min(height[a], height[b]))
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1

        return ans
