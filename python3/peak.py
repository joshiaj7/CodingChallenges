"""
Space    : O(1)
Time     : O(log n)
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        start = 0
        end = n-1

        while start < end:
            mid1 = (start + end) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                start = mid2
            else:
                end = mid1
        return start
