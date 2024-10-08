from typing import List
from bisect import bisect_left

"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n, 0, -1):
            k = bisect_left(nums, i)
            if (n-k) == i:
                return i
        
        return -1
