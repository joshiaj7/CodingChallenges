"""
Space    : O(n)
Time     : O(n)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        stack = []

        i, j = 0, 0
        while (i < m) or (j < n):
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    stack.append(nums1[i])
                    i += 1
                else:
                    stack.append(nums2[j])
                    j += 1
            elif i < m:
                stack.append(nums1[i])
                i += 1
            elif j < n:
                stack.append(nums2[j])
                j += 1

        for idx in range(len(nums1)):
            nums1[idx] = stack[idx]
