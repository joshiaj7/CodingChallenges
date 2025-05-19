from typing import List

"""
Space   : O(1)
Time    : O(1)
"""


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort(reverse=True)
        if nums[0] >= nums[1] + nums[2]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"

        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"

        return "scalene"
        