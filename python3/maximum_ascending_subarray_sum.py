from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)

        count = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                count += nums[i]
            else:
                count = nums[i]

            ans = max(ans, count)

        return ans
