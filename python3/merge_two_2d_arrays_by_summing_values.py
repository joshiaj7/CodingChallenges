from collections import defaultdict
from typing import List

"""
Space   : O(n+m)
Time    : O(n+m)
"""


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        d = defaultdict(int)

        for i, val in nums1:
            d[i] += val

        for i, val in nums2:
            d[i] += val

        for k, v in d.items():
            ans.append([k, v])

        ans.sort(key=lambda x: x[0])
        return ans
