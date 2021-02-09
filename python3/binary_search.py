"""
Space   : O(1)
Time    : O(log n)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end, prev_mid = 0, len(nums), -1000

        while start < end:
            mid = (start + end) // 2

            if mid == prev_mid:
                break

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
                prev_mid = mid
            elif nums[mid] < target:
                start = mid
                prev_mid = mid

        return -1

    def searchTemplate(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1
