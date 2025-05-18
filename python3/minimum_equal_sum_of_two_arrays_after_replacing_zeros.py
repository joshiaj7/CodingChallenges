from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = 0
        sum1 = 0
        for x in nums1:
            if x == 0:
                z1 += 1
            else:
                sum1 += x

        z2 = 0
        sum2 = 0
        for x in nums2:
            if x == 0:
                z2 += 1
            else:
                sum2 += x       

        if z2 == 0 and sum1 + z1 > sum2 + z2:
            return -1

        if z1 == 0 and sum1 + z1 < sum2 + z2:
            return -1

        return max(sum1 + z1, sum2 + z2)
        