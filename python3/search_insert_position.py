"""
Space   : O(1)
Time    : O(log n)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
