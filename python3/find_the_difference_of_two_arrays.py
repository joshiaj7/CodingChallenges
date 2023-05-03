"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        h1, h2 = {}, {}

        for x in nums1:
            h1[x] = 1

        for x in nums2:
            h2[x] = 1

        for k in h1.keys():
            if k not in h2:
                ans[0].append(k)

        for k in h2.keys():
            if k not in h1:
                ans[1].append(k)

        return ans
