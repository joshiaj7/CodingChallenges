from typing import List

"""
Space   : O(log n)
Time    : O(n log max(nums) + n log n)
"""

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        left, right = 0, nums[n-1] - nums[0] 
        while left < right:
            mid = (left + right) // 2
            k, i = 0, 1

            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    k += 1
                    i += 1
                i += 1

            if k >= p:
                right = mid
            else:
                left = mid + 1

        return left
