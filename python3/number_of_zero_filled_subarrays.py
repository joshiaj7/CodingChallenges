from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0 
        count = 0

        for x in nums:
            if x == 0:
                count += 1
                ans += count 
            else:
                count = 0

        return ans
