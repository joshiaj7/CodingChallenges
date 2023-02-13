"""
Space   : O(1)
Time    : O(1)
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high - low) // 2
        return ans + 1 if (low % 2 == 1) or (high % 2 == 1) else ans
