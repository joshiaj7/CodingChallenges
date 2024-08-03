from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
        