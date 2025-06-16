from collections import List

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, nums[j] - nums[i])

        return ans
        