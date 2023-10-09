from typing import List

"""
Space   : O(1)
Time    : O(log n)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums:
            return [-1, -1]

        n = len(nums)
        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[right] != target:
            return [-1, -1]

        ans[0] = right

        right = n-1
        while left < right:
            mid = ((left + right) // 2) + 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        ans[1] = right
        return ans

        