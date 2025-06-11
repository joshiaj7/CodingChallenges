from typing import List

"""
Space   : O(1)
Time    : O(log n)
"""

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # negative
        neg = n
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                neg = mid
                right = mid - 1
        
        # positive
        pos = n
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 1:
                left = mid + 1
            else:
                pos = mid
                right = mid - 1
        
        return max(n - pos, neg)
        