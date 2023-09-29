from typing import List

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        direction = 0

        for i in range(n-1):
            if direction != 0:
                if nums[i+1] - nums[i] < 0 and direction > 0:
                    return False
                if nums[i+1] - nums[i] > 0 and direction < 0:
                    return False

            if nums[i+1] - nums[i] != 0: 
                direction = nums[i+1] - nums[i]

        return True
        