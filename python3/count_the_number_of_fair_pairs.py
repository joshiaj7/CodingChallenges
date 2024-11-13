from bisect import bisect_left, bisect_right
from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()

        n = len(nums)
        for i in range(n-1):
            low = bisect_left(nums, lower - nums[i], i + 1)
            up = bisect_right(nums, upper - nums[i], i + 1)
            ans += up - low
            
        return ans
        