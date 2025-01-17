from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xorsum = 0
        for x in derived:
            xorsum ^= x

        return True if xorsum == 0 else False
