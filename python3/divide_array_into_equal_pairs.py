from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        for k, v in d.items():
            if v % 2 == 1:
                return False
            
        return True
