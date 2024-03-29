from typing import List

"""
Space   : O(1)
Time    : O(n)

Method:
Floyd's Tortoise and Hare Algorithm
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow
