from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        par = nums[0] % 2
        for i in range(1, n):
            if par == nums[i] % 2:
                return False

            par = nums[i] % 2
            

        return True
