"""
Space    : O(m)
Time     : O(m + n)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        buf = nums1[:m]

        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if buf[p1] < nums2[p2]:
                nums1[p1 + p2] = buf[p1]
                p1 += 1
            else:
                nums1[p1 + p2] = nums2[p2]
                p2 += 1

        while p1 < m:
            nums1[p1 + p2] = buf[p1]
            p1 += 1

        while p2 < n:
            nums1[p1 + p2] = nums2[p2]
            p2 += 1
