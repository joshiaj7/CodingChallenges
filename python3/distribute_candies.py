"""
Space   : O(1)
Time    : O(1)
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
