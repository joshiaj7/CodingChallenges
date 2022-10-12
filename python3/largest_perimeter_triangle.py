"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()

        for i in range(n-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                ans = max(ans, nums[i] + nums[i-1] + nums[i-2])

        return ans
