"""
Space   : O(1)
Time    : O(log n)
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        ans = 0
        left, right = 0, n-1

        while left <= right:
            mid = ((left + right) >> 2) << 1
            if mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid - 1
                ans = nums[mid]

        return ans
