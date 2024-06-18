from typing import List

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        a = set(nums1)
        b = set(nums2)
        
        for x in list(a):
            if x in b:
                ans.append(x)

        return ans
