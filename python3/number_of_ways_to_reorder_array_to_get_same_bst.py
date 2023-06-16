from typing import List
from math import comb

"""
Space   : O(n)
Time    : O(n^2)
"""


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def recurse(nums):
            if len(nums) <= 2:
                return 1

            left, right = [], []
            for num in nums:
                if num < nums[0]:
                    left.append(num)
                if num > nums[0]:
                    right.append(num)

            return comb(len(left) + len(right), len(right)) * recurse(left) * recurse(right)

        return (recurse(nums)-1) % ((10 ** 9) + 7)
