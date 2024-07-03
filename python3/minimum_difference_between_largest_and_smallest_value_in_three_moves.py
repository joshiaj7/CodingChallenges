from typing import List

"""
Space   : O(1)
Time    : O(n log n)
"""


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        ans = float('inf')
        nums.sort()
        
        start, end = 3, n-1
        for i in range(4):
            ans = min(ans, nums[end-i] - nums[start-i]) 

        return ans
