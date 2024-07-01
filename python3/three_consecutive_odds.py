from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for x in arr:
            if x % 2 == 1:
                count += 1
            else:
                count = 0

            if count >= 3:
                return True

        return False
            
        