from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        d1, d2 = {}, {}
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        for k, v1 in d1.items():
            if k in d2:
                v2 = d2[k]
                ans += [k] * min(v1, v2)

        return ans
        